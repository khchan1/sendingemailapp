import os
from flask import Flask, render_template, request
from flask_mail import Mail,Message # pip install flask_mail
import requests

app = Flask(__name__) #Initialise app


# Config
MAILGUN_API_KEY = os.environ.get("MAILGUN_API_KEY")
MAILGUN_PUBLIC_KEY =  os.environ.get("MAILGUN_PUBLIC_KEY")
MAILGUN_DOMAIN =  os.environ.get("MAILGUN_DOMAIN")
MAILGUN_SMTP_LOGIN = os.environ.get("MAILGUN_SMTP_LOGIN")
MAILGUN_SMTP_PASSWORD = os.environ.get("MAILGUN_SMTP_PASSWORD")
MAILGUN_SMTP_PORT = os.environ.get("MAILGUN_SMTP_PORT")
MAILGUN_SMTP_SERVER = os.environ.get("MAILGUN_SMTP_SERVER")

def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/" + str(MAILGUN_DOMAIN) + "/messages",
		auth=("api", MAILGUN_API_KEY),
		data={"from": "mailgun@" + str(MAILGUN_DOMAIN),
			"to": ["herokutext@gmail.com"],
			"subject": "Sending function - Testing",
			"text": "Testing 123"})



@app.route('/', methods = ['GET', 'POST'])
def result():
    if request.method == 'POST':
        #email = request.form['email']
        #subject = request.form['subject']
        #message = request.form['message']

        #msg = Message(subject, sender = 'billy.chan@macys.com' , recipients = [email])
        #msg.body = message
        #mail.send(msg)
        send_simple_message()
        return render_template('index.html', sent = True)
    else:
        return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)