import sys
import pandas 
from pandas import DataFrame
#from flask_login import UserMixin
from datetime import datetime
from app import db
from wtforms import SelectField

class Account(db.Model):
    """
    Create an Contract table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    idnumber= db.Column(db.Integer)
    email = db.Column(db.String(60), index=True, unique=True)
    balance = db.Column(db.Integer)
    pin =db.Column(db.String(4))
    created_at = db.Column(db.DateTime,index=False,unique=False,nullable=False, default=datetime.utcnow)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    email = db.Column(db.String(60), index=True, unique=True)
    phone = db.Column(db.String(10))
    transactions = db.relationship('Transaction', backref='account',lazy='dynamic')
	

class Transaction(db.Model):
    """
    Create an Contract table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model

    __tablename__ = 'transactions'
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    #trans_type = SelectField('Types', choices = [('withdraw','deposit','transfer','checkBalance')])
    accounts_id = db.Column(db.Integer, db.ForeignKey('accounts.id'))
    amount = db.Column(db.Integer, nullable=False)
    t_time= db.Column(db.Integer, default=0, nullable=False)
    #t_status = db.Column(db.Boolean,index=False,unique=False,nullable=False, default=True)
    trans_at= db.Column(db.DateTime,index=False,unique=False,nullable=False, default=datetime.utcnow)


