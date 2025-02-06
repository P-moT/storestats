from flask_app.models import users
from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt
import logging
import os
bcrypt = Bcrypt(app)

@app.route('/')
def home():
    if 'id' in session:
        if session['id'] == 1:
            return render_template('admin.html')
    else:
        return render_template('admin.html')

@app.route('/login', methods=['POST'])
def login():
    data = {
        'storeNumber': request.form['storeNumber'],
        'password': bcrypt.generate_password_hash(request.form['password']),
        'region': request.form['region'],
        'mgrName': request.form['mgrName']
    }

    if users.User.validate_form(data):
        id = users.User.create_user(data)
        session['id'] = id
    else:
        print('fail')
        return redirect('/')

    return redirect('/')
