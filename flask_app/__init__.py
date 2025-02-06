from flask import Flask
import logging
import os

logging.basicConfig(filename='record.log', level=logging.INFO, filemode='w')
app = Flask(__name__)
app.secret_key = os.getenv('App_Key')