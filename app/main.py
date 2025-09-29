from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel
import os
from app.email_utils import send_email
from dotenv import load_dotenv

load_dotenv()

API_SECRET_KEY = os.getenv("API_SECRET_KEY")

app = FastAPI(title="Mail Service API")

class EmailRequest(BaseModel):
    to: str
    subject: str
    body: str

@app.post()
def send_email_endpoint(email: EmailRequest, x_api_key: str = Header(None)):
    if x_api_key != API_SECRET_KEY:
        raise HTTPException(status_code=403, detail="Unauthorized")

    try:
        send_email(email.to, email.subject, email.body)
        return {"status": "success", "message": "Email sent"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
