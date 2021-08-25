from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required, Email, EqualTo
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators
from wtforms import ValidationError
from ..models.user import User
from ..models.roles import Role
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms import ValidationError
from ..models.user import User



class RegistrationForm(FlaskForm):
    
    def role_query():
        return Role.query

    role = QuerySelectField(query_factory=role_query, get_label='name', validators=[
                            validators.DataRequired()])
    first_name = StringField("First name", validators=[Required()])
    other_names = StringField("Other names", validators=[Required()])
    email = StringField('Your Email Address', validators=[Required(), Email()])
    username = StringField('Enter your username', validators=[Required()])
    password = PasswordField('Password', validators=[Required(), EqualTo(
        'password_confirm', message='Passwords must match')])
    password_confirm = PasswordField(
        'Confirm Passwords', validators=[Required()])
    submit = SubmitField('Register')

    def validate_email(self, data_field):
        if User.query.filter_by(email=data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self, data_field):
        if User.query.filter_by(username=data_field.data).first():
            raise ValidationError('That username is taken')


class LoginForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
