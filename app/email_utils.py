import resend
import os
from dotenv import load_dotenv

load_dotenv()

RESEND_API_KEY = os.getenv("RESEND_API_KEY")
resend.api_key = RESEND_API_KEY

FROM_EMAIL = os.getenv("FROM_EMAIL")

def send_email(to_email: str, subject: str, body: str):
    try:
        params: resend.Emails.SendParams = {
        "from": FROM_EMAIL,
        "to": [to_email],
        "subject": subject,
        "html": body
        }
        response = resend.Emails.send(params)
        return response
    except Exception as e:
        print(f"❌ Resend API error: {str(e)}")
        raise Exception(f"Resend API error: {str(e)}")
