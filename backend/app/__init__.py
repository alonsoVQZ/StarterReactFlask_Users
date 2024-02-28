import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import DevelopmentConfig, ProductionConfig, TestingConfig
from models.user import User
from routes import api

load_dotenv()

app = Flask(__name__)

if os.environ.get('FLASK_ENV') == 'development':
    app.config.from_object(DevelopmentConfig)
elif os.environ.get('FLASK_ENV') == 'production':
    app.config.from_object(ProductionConfig)
elif os.environ.get('FLASK_ENV') == 'testing':
    app.config.from_object(TestingConfig)
    
db = SQLAlchemy(app)

Migrate(app, db)

login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(id):
    return User.get(id)

CORS(app, supports_credentials=True)

app.register_blueprint(api, url_prefix='/api')