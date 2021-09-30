from os import X_OK
from flask import render_template, redirect, request
from users_app import app
from users_app.models.user import User


@app.route ('/users/new', methods=['GET'])
def createpage():
    return render_template ('create.html')

@app.route ('/users', methods=['GET'])
def users_page():
    users = User.get_users_info()

    return render_template ('read.html', users = users)
    

@app.route ('/users/new', methods=['POST'])
def addNew():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']

    newUser = User(first_name,last_name,email)
    result = User.addUser(newUser)
    print (result)
    return redirect('/users')
