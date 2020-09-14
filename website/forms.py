from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField
from website.models import User, Dataset

class Register(FlaskForm):
    username = StringField('Email', validators=[DataRequired(), Length(min=5, max=20)])    
    password = PasswordField('Password', validators=[DataRequired(), Length(min=5, max=20)])
    confirm = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That email has already been used')


class Login(FlaskForm):
    username = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    rememberMe = BooleanField('Remember Me')
    submit = SubmitField('Sign In')  


class UploadForm(FlaskForm):
    title = StringField("Mean vesicle size (Rm)", validators=[DataRequired(), Length(min=5, max=20)])
    z = FileField("Distance from flat bilayer center (z vector)", validators=[DataRequired()])
    d = FileField("Domain scattering length density profile (d vector)", validators=[DataRequired()])
    m = FileField("Matrix (surround) scattering length density profile (m vector)", validators=[DataRequired()])
    s = FileField("Schulz distribution probabilities (s vector)", validators=[DataRequired()])
    t = FileField("Schulz distribution vesicle radii (t vector)", validators=[DataRequired()])
    w = FileField("Angular expansion coefficients (w~ vector, for l)", validators=[DataRequired()])
    rm = StringField("Mean vesicle size (Rm)", validators=[DataRequired()], Length(min=1, max=30))
    o = StringField("Relative polydispersity (o)", validators=[DataRequired(), Length(min=1, max=30)])
    ps = StringField("Solvent scattering length density (ps)", validators=[DataRequired(), Length(min=1, max=30)])
    ad = StringField("Domain area fraction (ad)", validators=[DataRequired(), Length(min=1, max=30)])

    submit = SubmitField('Submit')
    
    def validate_title(self, title):
        dataset = Dataset.query.filter_by(title=title.data).first()
        if dataset:
            raise ValidationError('That title is already taken')


