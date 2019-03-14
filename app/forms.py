from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, validators
from wtforms.validators import DataRequired
class WithdrawForm(FlaskForm):
    amount = IntegerField('AmountToWithdraw',[validators.NumberRange(min=200, max=10000)])
    submit = SubmitField('Withdraw')