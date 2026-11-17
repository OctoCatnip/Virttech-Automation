import requests
import time
import re
from datetime import datetime


class MailTm:

    BASE_URL = "https://api.mail.tm"

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.token = None
        self.session = requests.Session()

    def request_api(self, method, url, **kwargs):

        delay = 10

        for attempt in range(5):

            response = self.session.request(
                method,
                url,
                timeout=20,
                **kwargs
            )

            if response.status_code == 429:

                retry_after = response.headers.get("Retry-After")

                if retry_after and retry_after.isdigit():
                    wait_time = int(retry_after)
                else:
                    wait_time = delay

                print(f"Mail.tm rate limited. Waiting {wait_time} seconds...")

                time.sleep(wait_time)
                delay = min(delay * 2, 60)

                continue

            response.raise_for_status()
            return response

        raise Exception("Mail.tm API is still rate limiting requests.")

    @staticmethod
    def _coerce_text(value):
        if value is None:
            return ""
        if isinstance(value, str):
            return value
        if isinstance(value, list):
            return " ".join(part for part in (MailTm._coerce_text(item) for item in value) if part)
        if isinstance(value, dict):
            for key in ("content", "text", "html", "value"):
                if key in value:
                    text = MailTm._coerce_text(value[key])
                    if text:
                        return text
            return " ".join(
                part for part in (MailTm._coerce_text(v) for v in value.values()) if part
            )
        return str(value)

    def login(self):

        url = f"{self.BASE_URL}/token"

        response = self.request_api(
            "POST",
            url,
            json={
                "address": self.email,
                "password": self.password
            }
        )

        self.token = response.json()["token"]
        self.session.headers.update({"Authorization": f"Bearer {self.token}"})

        return self.token

    def get_messages(self):

        url = f"{self.BASE_URL}/messages"

        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        response = self.request_api(
            "GET",
            url,
            headers=headers
        )

        return response.json()["hydra:member"]

    def get_message_details(self, message_id):

        url = f"{self.BASE_URL}/messages/{message_id}"

        headers = {
            "Authorization": f"Bearer {self.token}"
        }

        response = self.request_api(
            "GET",
            url,
            headers=headers
        )

        return response.json()

    def get_otp(self, since_timestamp, timeout=120):

        start_time = time.time()
        checked_messages = set()

        while time.time() - start_time < timeout:

            messages = self.get_messages()

            for message in messages:

                message_id = message.get("id")
                if not message_id:
                    continue

                # Skip messages already checked
                if message_id in checked_messages:
                    continue

                checked_messages.add(message_id)

                created_at = message.get("createdAt")
                if not created_at:
                    continue

                try:
                    received_time = datetime.fromisoformat(
                        created_at.replace("Z", "+00:00")
                    ).timestamp()
                except ValueError:
                    continue

                if received_time < since_timestamp:
                    continue

                details = self.get_message_details(message_id)
                if not isinstance(details, dict):
                    continue

                email_text = " ".join(
                    part for part in (
                        self._coerce_text(details.get("text")),
                        self._coerce_text(details.get("html")),
                    ) if part
                )

                match = re.search(r"(?<!\d)(\d{6})(?!\d)", email_text)

                if match:
                    return match.group(1)

            print("Waiting for OTP email...")
            time.sleep(10)

        raise TimeoutError("OTP was not received within the time limit.")
