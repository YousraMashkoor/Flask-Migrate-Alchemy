from flask import Blueprint
from flask_restful import Api
from .account import CreateAccount

account_bp = Blueprint('account_bp',__name__)

account_api = Api(account_bp)
account_api.add_resource(CreateAccount,'/accounts')


from .base import base_bp