from flask import request
from flask_restful import Resource

from app import db
from app.models.account import Account


class CreateAccount(Resource):

    def post(self):
        account = Account(
            account_id = request.json['account_id'],
            status = request.json['status'],
            balance = request.json['balance']
        )
        db.session.add(account)
        db.session.commit()

        output = {
            'message': 'Account Created',
            'resource_id': account.account_id,
            'status': 200
        }

        return output


    def get(self):
        accounts = Account.query.all()
        data=[]
        for account in accounts:
            record = {
                "account_id" : account.account_id,
                "status" : account.status.value,
                "balance" : account.balance,
            }

            data.append(record)

        return {
            'count': len(data),
            'num_results': len(data),
            'objects': data,
        }

