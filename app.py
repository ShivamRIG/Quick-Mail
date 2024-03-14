from flask import Flask ,render_template, request
from emailauto import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('welcome.html')

@app.route("/email")
def Email():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    email = request.form.get('email')
    subject = request.form.get('subject')
    body = request.form.get('body')
    email_send(None,subject,email,body)
    
    # Do something with the form data (e.g., send email)
    print("Received email:", email)
    print("Subject:", subject)
    print("Body:", body)
    
    # Redirect to a success page or return a response
    return render_template('Submit.html')


    