from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
import logging
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
db = "storestats"

class User:
    def __init__(self):
        pass

    @staticmethod
    def validate_form(data):
        valid = True
        if len(data['storeNumber']) > 4:
            flash('Please enter a valid Store Number', 'error')
            valid = False
        if len(data['storeNumber']) < 1:
            flash('Please enter a valid Store Number', 'error')
        if len(data['password']) < 1:
            flash('Please enter a password', 'error')
        return valid

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (storeNumber, password, region, mgrName) VALUES (%(storeNumber)s, %(password)s, %(region)s, %(mgrName)s);"
        print(query)
        return connectToMySQL(db).query_db(query, data)