from flask import Flask, request, redirect, render_template, session, flash
#bot the following lines are needed to verify emails
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

app=Flask(__name__)
app.secret_key=("somekey")

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/process', methods=['POST'])
def process():
    if len(request.form['email'])<1 or len(request.form['first_name'])<1 or len(request.form['last_name'])<1 or len(request.form['password'])<1 or len(request.form['confirm_password'])<1:
        flash("All fields are required and must not be blank")
        return redirect ('/')
    elif request.form['first_name'].isalpha() == False or request.form['last_name'].isalpha() == False:
        flash("First and Last Name cannot contain any numbers")
        return redirect ('/')
    elif len(request.form['password'])<9:
        flash("Password should be more than 8 characters")
        return redirect ('/')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address")
        return redirect ('/')
    elif request.form['password'] != request.form['confirm_password']:
        flash("Password and Password Confirmation should match")
        return redirect ('/')
    else: 
        flash("Successfully Submitted")
        return redirect ('/')
app.run(debug=True)