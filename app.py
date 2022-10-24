from flask import Flask, render_template, request
from flask_mail import Mail,Message # pip install flask_mail
import requests

app = Flask(__name__) #Initialise app


# Config
app.config['MAIL_SERVER'] = "smtp.mailgun.org"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'postmaster@sandbox8706cdc9df464716bd0a18de0fa513e2.mailgun.org'
app.config['MAIL_PASSWORD'] = 'ad506e5a52225d602b0c0e3cb4fc5285-8845d1b1-7aa456ad'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = False
mail = Mail(app) # Instance

def send_simple_message():
	return requests.post(
		"https://api.mailgun.net/v3/index-send/messages",
		auth=("api", "5f143565005ce4f6d999f47f42de8593-8845d1b1-88c9d249"),
		data={"from": "billy.chan@macys.com",
			"to": ["billy.chan@macys.com", "billy.chan@macys.com"],
			"subject": "Hello",
			"text": "Testing some Mailgun awesomness!"})



@app.route('/', methods = ['GET', 'POST'])
def result():
    if request.method == 'POST':
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        msg = Message(subject, sender = 'billy.chan@macys.com' , recipients = [email])
        msg.body = message
        mail.send(msg)
        return render_template('index.html', sent = True)
    else:
        return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
