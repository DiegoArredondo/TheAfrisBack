from flask import Flask
from flask_orator import Orator
from app import db_config

app = Flask(__name__)

app.config['ORATOR_DATABASES']= db_config.db_config
db= Orator(app)
