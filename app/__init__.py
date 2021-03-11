import flask
import os
import enum
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # DATABASE_URL = f"postgresql://{os.environ.get('DB_USER')}:{os.environ.get('DB_PASSWORD')}@{os.environ.get('DB_HOST')}/{os.environ.get('DB_NAME')}"
    DATABASE_URL = f"postgresql://postgres:postgres@localhost/test3"

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)


    # class Status(enum.Enum):
    #     due = 'due'
    #     clear = 'clear'
    #     extra = 'extra'

    # class Account(db.Model):
    #     __tablename__ = 'account'

    #     account_id = db.Column(db.String(12), primary_key=True)
    #     balance = db.Column(db.Integer)
    #     status = db.Column(db.Enum(Status), default=Status.clear)



    from .views import base_bp
    
    app.register_blueprint(base_bp, url_prefix='/')


    return app