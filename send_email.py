import smtplib, ssl
import os

print(os.getenv("PASSWORD"))
def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    user_name = "daniele.santagati@gmail.com"
    password = os.getenv("PASSWORD")

    receiver = "daniele.santagati@gmail.com"
    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver, message)



