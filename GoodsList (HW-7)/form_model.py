from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, HiddenField, SubmitField


class MyInputForm(FlaskForm):
    id_field = HiddenField()
    title = StringField('Title')
    amount = IntegerField('Amount')
    price = FloatField('Price')
    category = StringField('Category')
    buyer = StringField('Buyer')
    submit = SubmitField('Add/Update Record')

