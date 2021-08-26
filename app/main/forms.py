from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,IntegerField,FileField
from wtforms.validators import Required, InputRequired
from wtforms import ValidationError

class NewJobForm(FlaskForm):
    '''
    Class that creates new job form
    ''' 
    # job_id = IntegerField("Job id", validators=[InputRequired()])
    commitment = StringField("Commitment", validators=[Required()])
    department = StringField("Department", validators=[Required()])
    team = StringField("Team", validators=[Required()])
    location = StringField("Location", validators=[Required()])
    descriptionPlain = TextAreaField("Description", validators=[Required()])

    submit = SubmitField('Add job')

class UpdateProfile(FlaskForm):
    profile_pic_path= FileField('Update your profile pic')
    submit = SubmitField('Submit')


class UpdateBio(FlaskForm):
    bio = TextAreaField('Bio',validators = [Required()])
    # submit = SubmitField('Submit'
