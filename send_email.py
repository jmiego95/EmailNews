import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "voxxympgh@gmail.com"
    password = "jddcwejoxmqogcos"
    receiver = "pythonapp2000@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
