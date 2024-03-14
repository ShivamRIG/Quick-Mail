import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv

load_dotenv()
def email_send(img_path=None, Subject=None,TO=None ,Body=None):
    # Retrieve email address and password from environment variables
    email_address = os.getenv('EMAIL_ADDRESS')
    email_password =os.getenv('EMAIL_PASSWORD')

    if not email_address or not email_password:
        print("Email address or password not found in environment variables.")
        sys.exit(1)

    msg = MIMEMultipart()
    msg['Subject'] = Subject
    msg['From'] = email_address
    msg['To'] = TO


    if img_path:
        # If image path is provided, attach the image
        filename = os.path.basename(img_path)
        with open(img_path, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
            )
            msg.attach(part)
    else:
        # If no image path is provided, send a simple text email
        body = Body
        msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:     
        smtp.login(email_address, email_password)
        smtp.send_message(msg)
        print("Email sent")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("Usage: python script.py [image_path]")
        sys.exit(1)

    img_path = sys.argv[1] if len(sys.argv) == 2 else None
    
