# TAP Selenium Automation

This project automates a partner registration flow with Selenium and temporary email accounts from mail.tm.

## Project purpose
The automation covers the signup and OTP validation flow, then moves through the registration forms until the Experience and Performance Metrics step.

## Environment and setup

### Language
- Python 3.14.4

### Framework and tools
- Selenium WebDriver
- Pytest
- Requests
- Chrome browser automation

### Browser and driver version
- Browser: Google Chrome / Chromium
- Driver: ChromeDriver must match the installed Chrome version
- Recommended setup:
  - Install the matching Chrome version
  - Download the corresponding ChromeDriver
  - Add ChromeDriver to your system PATH or use the matching version in your local environment

## Dependencies
The project uses:
- selenium
- pytest
- requests

## Install
```powershell

python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requriment.txt
```

## Run the script
```powershell

.\.venv\Scripts\Activate.ps1
pytest tests/test_signin_page.py -q
```

## Temporary email usage
This project uses temporary email accounts from mail.tm to receive OTP codes during sign-up.

Example flow:
- create a temp mail account
- log in through Mail.tm API
- wait for the registration email
- read the 6-digit OTP
- continue the Selenium flow

## Current status / note
The automation was developed and tested up to the Experience and Performance Metrics step.

Important blockers in the current environment:
- the public IP was blocked or blacklisted after repeated attempts
- mail.tm also rate-limited OTP checks and temp-mail access during heavy use
- the Experience and Performance Metrics selector step is blocked by a custom dropdown / year-value issue, so the automation stops before the next form is submitted
- because of this, the flow was not completed fully beyond the experience page in the current environment

This blocker is specific to the experience field value selection, not to the login or OTP flow itself.

