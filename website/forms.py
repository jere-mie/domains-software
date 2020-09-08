from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField, StringField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError

class UploadForm(FlaskForm):
    z = FileField("Distance from flat bilayer center (z vector)", validators=[DataRequired()])
    d = FileField("Domain scattering length density profile (d vector)", validators=[DataRequired()])
    m = FileField("Matrix (surround) scattering length density profile (m vector)", validators=[DataRequired()])
    s = FileField("Schulz distribution probabilities (s vector)", validators=[DataRequired()])
    t = FileField("Schulz distribution vesicle radii (t vector)", validators=[DataRequired()])
    w = FileField("Angular expansion coefficients (w~ vector, for l)", validators=[DataRequired()])
    rm = StringField("Mean vesicle size (Rm)", validators=[DataRequired()])
    o = StringField("Relative polydispersity (o)", validators=[DataRequired()])
    ps = StringField("Solvent scattering length density (ps)", validators=[DataRequired()])
    ad = StringField("Domain area fraction (ad)", validators=[DataRequired()])

    submit = SubmitField('Submit')

