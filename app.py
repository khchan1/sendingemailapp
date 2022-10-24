from flask import Flask, render_template, request
from flask_mail import Mail,Message # pip install flask_mail

app = Flask(__name__) #Initialise app


# Config
app.config['MAIL_SERVER'] = "appmailos.federated.fds"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'billy.chan@macys.com'
app.config['MAIL_PASSWORD'] = 'D70364.ok'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = False
mail = Mail(app) # Instance



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
