from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import Required, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User

class LoginForm(Form):
    email = StringField('Email', validators = [Required(), Length(1, 64),
                        Email()])
    password = PasswordField('Password', validators = [Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

class RegistrationForm(Form):
    email = StringField('Email', validators = [Required(), Length(1, 64),
                        Email()])
    username = StringField('Username', validators = [Required(),
                            Length(1,64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$',
                                            0,'Username must only have letters, ' 
                                            'numbers,dots or underscores')])
    password = PasswordField('Password', validators = [
            Required(), EqualTo('password2',message='Password must match.')])
    password2 = PasswordField('Confirm Password',validators = [Required()])
    submit = SubmitField('Register')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email has already registered.')
    
    def validate_username(self,field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError('Username already in use.')

class ChangePasswordForm(Form):
    old_password = PasswordField('Old password', validators=[Required()])
    password = PasswordField('New Password', validators = [
            Required(), EqualTo('password2',message='Password must match.')])
    password2 = PasswordField('Confirm Password', validators = [Required()])
    submit = SubmitField('Update Password')

class PasswordResetRequestForm(Form):
    email = StringField('Email', validators = [Required(), Length(1, 64),
                        Email()])
    submit = SubmitField('Reset Password')

class PasswordResetForm(Form):
    email = StringField('Email', validators = [Required(), Length(1, 64),
                        Email()])
    
    password = PasswordField('Password', validators = [
            Required(), EqualTo('password2',message='Password must match.')])
    password2 = PasswordField('Confirm Password', validators = [Required()])
    submit = SubmitField('Reset Password')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first() is None:
            raise ValidationError('Unknown email address.')
    
class ChangeEmailForm(Form):
    email = StringField('Email', validators = [Required(), Length(1, 64),
                        Email()])
    password = PasswordField('Password', validators = [Required()])
    submit = SubmitField('Change Email')

    def validate_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email has already registered.')


