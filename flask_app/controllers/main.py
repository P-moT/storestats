from flask_app.models import users
from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_bcrypt import Bcrypt
from flask_app.controllers.data import fiscalday
import logging
import os
bcrypt = Bcrypt(app)

@app.route('/')
def home():
    print(session)
    if 'id' in session:
        if session['id'] == 1:
            print("admin view activated")
            return render_template('admin.html')
        else:
            user = users.User.getUserById({'id':session['id']})
            return render_template('home.html', user = user)
    else:
        print(session)
        data = {
            'year': 2025,
            'month': 1,
            'day': 21
        }
        fiscalday(data)
        return render_template('login.html')

@app.route('/createuser', methods=['POST'])
def create():
    data = {
        'storeNumber': request.form['storeNumber'],
        'password': bcrypt.generate_password_hash(request.form['password']),
        'region': request.form['region'],
        'mgrName': request.form['mgrName']
    }
    print(data)
    if users.User.validateForm(data):
        id = users.User.createUser(data)
        print("creating user")
        session['id'] = id
    else:
        print('fail')
        return redirect('/')
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    data = {
        'storeNumber': request.form['storeNumber'],
    }
    checkUser = users.User.getUserByStoreNumber(data)
    if not checkUser:
        flash("Invalid credentials", "error")
        return redirect('/')
    if not bcrypt.check_password_hash(checkUser['password'], request.form['password']):
        flash("Invalid Credentials", "error")
        return redirect('/')
    session['id'] = checkUser['id']
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
