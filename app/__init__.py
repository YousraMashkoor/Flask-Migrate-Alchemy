import flask
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "test.db"

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql:////{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .views import base_bp
    
    app.register_blueprint(base_bp, url_prefix='/')


    return app