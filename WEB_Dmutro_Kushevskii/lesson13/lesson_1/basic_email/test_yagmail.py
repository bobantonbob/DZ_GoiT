import yagmail

# Email configuration
sender_email = "sndr"
receiver_email = "recv"
password = "pswd"

# Create yagmail object
yag = yagmail.SMTP(sender_email, password)

# Send email
yag.send(
    to=receiver_email,
    subject="Subject of the Email",
    contents="This is the body of the email"
)
