import os
from flask import Flask, render_template, request
from flask_mail import Mail,Message # pip install flask_mail
import requests
import smtplib, ssl

app = Flask(__name__) #Initialise app


# Config - Mailgun
MAILGUN_API_KEY = os.environ.get("MAILGUN_API_KEY")
MAILGUN_PUBLIC_KEY =  os.environ.get("MAILGUN_PUBLIC_KEY")
MAILGUN_DOMAIN =  os.environ.get("MAILGUN_DOMAIN")
MAILGUN_SMTP_LOGIN = os.environ.get("MAILGUN_SMTP_LOGIN")
MAILGUN_SMTP_PASSWORD = os.environ.get("MAILGUN_SMTP_PASSWORD")
MAILGUN_SMTP_PORT = os.environ.get("MAILGUN_SMTP_PORT")
MAILGUN_SMTP_SERVER = os.environ.get("MAILGUN_SMTP_SERVER")


# Mailgun Send Email Function
def send_simple_message_mailgun(email, subject, message):
	return requests.post(
		"https://api.mailgun.net/v3/" + str(MAILGUN_DOMAIN) + "/messages",
		auth=("api", MAILGUN_API_KEY),
		data={"from": "mailgun@" + str(MAILGUN_DOMAIN),
			"to": [email],
			"subject": subject,
			"text": message})

# Config - Cloudmailin
CLOUDMAILIN_FORWARD_ADDRESS = os.environ.get("CLOUDMAILIN_FORWARD_ADDRESS")
CLOUDMAILIN_PASSWORD =  os.environ.get("CLOUDMAILIN_SEND_PASSWORD")
CLOUDMAILIN_SECRET =  os.environ.get("CLOUDMAILIN_SECRET")
CLOUDMAILIN_USERNAME =  os.environ.get("CLOUDMAILIN_SEND_USERNAME")

# Cloudmailin
def send_simple_message_cloud():
    hostname = "smtp.cloudmta.net"
    username = CLOUDMAILIN_USERNAME
    password = CLOUDMAILIN_PASSWORD

    message = ("""\
Subject: Test from Python
To: herokutext@gmail.com
From: from@example.com

This message is sent from Python.""")

    server = smtplib.SMTP(hostname, 587)
    server.ehlo() # Can be omitted
    server.starttls(context=ssl.create_default_context()) # Secure the connection
    server.login(username, password)
    server.sendmail("from@cloudmailin.com", "herokutext@gmail.com", message)
    server.quit



@app.route('/', methods = ['GET', 'POST'])
def result():
    if request.method == 'POST':
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        #msg = Message(subject, sender = 'billy.chan@macys.com' , recipients = [email])
        #msg.body = message
        #mail.send(msg)
        send_simple_message_cloud()
        return render_template('index.html', sent = True)
    else:
        return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)