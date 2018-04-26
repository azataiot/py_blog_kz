# coding: utf-8
from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email


class LoginForm(Form):
    email = StringField(u'Электрондық пошта', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    password = PasswordField(u'пароль', validators=[DataRequired()])
