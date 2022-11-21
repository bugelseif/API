from flask_wtf import FlaskForm, Form
from wtforms import SelectField, SubmitField, StringField
from wtforms.validators import DataRequired


class EscolhaCidade(FlaskForm):
    cidades = open("app\process\cidades.txt", 'r').readlines()
    choices = []
    for i in cidades:
        city = (i.rstrip('\n'),i)
        choices.append(city)
    
    cidade = SelectField(u'cidade', choices=choices)
    submit = SubmitField('Sign In')

class EscolhaCoordenadas(FlaskForm):
    longitude = StringField(u'longitude')
    latitude = StringField(u'latitude')
    submit = SubmitField('Acessar')