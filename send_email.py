import os
import smtplib
from email.message import EmailMessage

def send_email(subject: str, body: str, to_emails: list[str]) -> None:
    """
    Send an email via Gmail SMTP.
    
    Requires the environment variables:
      GMAIL_ADDRESS    — your full Gmail address (e.g. you@gmail.com)
      GMAIL_APP_PASS   — your Gmail app password or account password
    """
    # Load credentials from environment
    gmail_address = "andres.daniel.loza.c@gmail.com"
    gmail_pass = "ajcy rqyn cabi ksht"
    if not gmail_address or not gmail_pass:
        raise ValueError("Set GMAIL_ADDRESS and GMAIL_APP_PASS environment variables")

    # Create the email
    msg = EmailMessage()
    msg["From"] = gmail_address
    msg["To"] = ", ".join(to_emails)
    msg["Subject"] = subject
    msg.set_content(body)

    # Connect to the Gmail SMTP server and send
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(gmail_address, gmail_pass)
        smtp.send_message(msg)
        print(f"Email sent to {to_emails}")

if __name__ == "__main__":
    # Example usage
    subject = "Hello from Python!"
    body = """\
Hi there,

This is a test email sent from a Python script using Gmail.
Feel free to customize this message.

Best,
Your Python Script
"""
    recipients = ["andres.daniel.loza.c@gmail.com"]
    
    try:
        send_email(subject, body, recipients)
    except Exception as e:
        print(f"Error sending email: {e}")
