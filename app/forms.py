from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class QuestionForm(FlaskForm):
    subject = StringField('TITLE', validators=[DataRequired('subject is req')])
    content = TextAreaField('CONTENT', validators=[DataRequired('content!!')])

class AnswerForm(FlaskForm):
    content = TextAreaField('CONtent', validators=[DataRequired('CONTENT!')])

class UserCreateForm(FlaskForm):
    username = StringField('USERNAME', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('PASSWORD', validators=[DataRequired(), EqualTo('password2', 'PW does not match')])
    password2 = PasswordField('Check PW', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])

class UserLoginForm(FlaskForm):
    username = StringField('USERNAME', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('PASSWORD', validators=[DataRequired()])

class CommentForm(FlaskForm):
    content = TextAreaField('내용', validators=[DataRequired()])
