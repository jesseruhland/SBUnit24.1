from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class PetForm(FlaskForm):
    """form for pet entry/edits"""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[('dog', 'dog'), ('cat','cat'), ('mouse', 'mouse'), ('pig', 'pig'), ('porcupine', 'porcupine')])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Notes", validators=[Optional()])
    available = BooleanField("This Pet Is Available")
