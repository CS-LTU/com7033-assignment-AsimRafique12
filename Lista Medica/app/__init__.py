from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from flask_login import LoginManager

db = SQLAlchemy()
mongo = PyMongo()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)  
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/patients'

    db.init_app(app)
    mongo.init_app(app)
    login_manager.init_app(app)

    return app