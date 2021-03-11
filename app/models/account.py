from app import db

'''
Defining enum: Status
'''
class Status(enum.Enum):
    due = 'due'
    clear = 'clear'
    extra = 'extra'

class Account(db.Model):
    __tablename__ = 'account'

    account_id = db.Column(db.String(12), primary_key=True)
    balance = db.Column(db.Integer)
    status = db.Column(db.Enum(Status), default=Status.clear)

