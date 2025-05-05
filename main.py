from fastapi import FastAPI
from pydantic import BaseModel
from send_email import send_email


class Message(BaseModel):
    subject: str
    body: str 
    to_emails: list[str]
    


app = FastAPI()


@app.post("/")
async def create_item(message: Message):
    try:
        send_email(message.subject, message.body, message.to_emails)
    except Exception as e:
        return {"error": str(e)}
    return {"message": "Email sent successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
