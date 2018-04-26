#coding:utf-8
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, Optional


class CommentForm(Form):
    name = StringField(u'Aты', validators=[DataRequired()])
    email = StringField(u'Электрондық пошта', validators=[DataRequired(), Length(1, 64),
                                            Email()])
    content = TextAreaField(u'Мазмұны', validators=[DataRequired(), Length(1, 1024)])
    follow = StringField(validators=[DataRequired()])
