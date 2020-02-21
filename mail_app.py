# from flask import Flask
# from flask_mail import Mail, Message
#
# app =Flask(__name__)
#
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'
# app.config['MAIL_PORT'] = 465
# app.config['MAIL_USERNAME'] = 'sharmagaurang612@gmail.com'
# app.config['MAIL_PASSWORD'] = '8865083915'
# app.config['MAIL_USE_TLS'] = False
# app.config['MAIL_USE_SSL'] = True
#
# mail = Mail(app)
#
#
# @app.route("/")
# def index():
#     msg = Message('Hello', sender='sharmagaurang612@gmail.com', recipients=['gaurang.sharma7065@gmail.com'])
#     msg.body = "This is the email body"
#     print(msg)
#     mail.send(msg)
#     print("sent")
#     return "Sent"
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

import smtplib

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>This is headline.</h1>
"""

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender='sharmagaurang612@gmail.com', receivers='', message)
    print("Successfully sent email")
except SMTPException:
    print("Error: unable to send email")
