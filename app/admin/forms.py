# coding:utf-8
from flask.ext.wtf import Form
from wtforms import SelectField, StringField, TextAreaField, SubmitField, \
    PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from ..main.forms import CommentForm


class CommonForm(Form):
    types = SelectField(u'Блог санаты', coerce=int, validators=[DataRequired()])
    source = SelectField(u'Блогтың көзі', coerce=int, validators=[DataRequired()])


class SubmitArticlesForm(CommonForm):
    title = StringField(u'Атауы', validators=[DataRequired(), Length(1, 64)])
    content = TextAreaField(u'Блог мазмұны', validators=[DataRequired()])
    summary = TextAreaField(u'Бауэн дерексіз', validators=[DataRequired()])


class ManageArticlesForm(CommonForm):
    pass


class DeleteArticleForm(Form):
    articleId = StringField(validators=[DataRequired()])


class DeleteArticlesForm(Form):
    articleIds = StringField(validators=[DataRequired()])


class DeleteCommentsForm(Form):
    commentIds = StringField(validators=[DataRequired()])


class AdminCommentForm(CommentForm):
    article = StringField(validators=[DataRequired()])


class AddArticleTypeForm(Form):
    name = StringField(u'Жіктеу атауы', validators=[DataRequired(), Length(1, 64)])
    introduction = TextAreaField(u'Жіктеуді енгізу')
    setting_hide = SelectField(u'Сипаттар', coerce=int, validators=[DataRequired()])
    menus = SelectField(u'Навигация', coerce=int, validators=[DataRequired()])
# You must add coerce=int, or the SelectFile validate function only validate the int data


class EditArticleTypeForm(AddArticleTypeForm):
    articleType_id = StringField(validators=[DataRequired()])


class AddArticleTypeNavForm(Form):
    name = StringField(u'Шарлау атауы', validators=[DataRequired(), Length(1, 64)])


class EditArticleNavTypeForm(AddArticleTypeNavForm):
    nav_id = StringField(validators=[DataRequired()])


class SortArticleNavTypeForm(AddArticleTypeNavForm):
    order = StringField(u'Жоқ.', validators=[DataRequired()])


class CustomBlogInfoForm(Form):
    title = StringField(u'Блог атауы', validators=[DataRequired()])
    signature = TextAreaField(u'Жеке қолтаңба', validators=[DataRequired()])
    navbar = SelectField(u'Навигациялық стиль', coerce=int, validators=[DataRequired()])


class AddBlogPluginForm(Form):
    title = StringField(u'Плагин атауы', validators=[DataRequired()])
    note = TextAreaField(u'Ескерту')
    content = TextAreaField(u'Мазмұны', validators=[DataRequired()])


class ChangePasswordForm(Form):
    old_password = PasswordField(u'Бастапқы құпия сөз', validators=[DataRequired()])
    password = PasswordField(u'Жаңа құпия сөз', validators=[
        DataRequired(), EqualTo('password2', message=u'Қате пароль енгізу екі рет!')])
    password2 = PasswordField(u'Жаңа құпия сөзді растаңыз', validators=[DataRequired()])


class EditUserInfoForm(Form):
    username = StringField(u'Бүркеншік аты', validators=[DataRequired()])
    email = StringField(u'Электрондық пошта', validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField(u'Құпия сөзді растау', validators=[DataRequired()])
