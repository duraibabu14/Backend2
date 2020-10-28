from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired, Length, Email, ValidationError
from website.models import User


class RegistrationForm(FlaskForm):
    username=StringField('Fullname',validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    note = StringField('Leave a Note...', validators=[DataRequired(),Length(min=2,max=120)])
    send=SubmitField('Send')

    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This Name is Taken Please Choose an another')

    def validate_email(self,email):
        email=User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('This Email is Taken Please Choose an another')
    def validate_note(self,note):
        note=User.query.filter_by(email=note.data).first()
        if note:
            raise ValidationError('This note is already written Please Write something else')
