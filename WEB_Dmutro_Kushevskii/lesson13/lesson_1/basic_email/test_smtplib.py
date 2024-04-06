import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "fatsapiuser@meta.ua"
receiver_email = "dima.kushhevskij@gmail.com"
password = "pythonCourse2023"

# Create message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Subject of the Email"

# Add body to email
body = "This is the body of the email"
message.attach(MIMEText(body, "plain"))

# Connect to SMTP server
with smtplib.SMTP_SSL("smtp.meta.ua", 465) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
