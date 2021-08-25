from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,IntegerField
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

# class BlogForm(FlaskForm):

#  title = StringField('Blog title',validators=[Required()])

#  author = StringField('Name',validators=[Required()])

#  review = TextAreaField('Write blog here: ')

#  submit = SubmitField('Submit')



# class UpdateProfile(FlaskForm):
#     bio = TextAreaField('Tell us about you.',validators = [Required()])
#     submit = SubmitField('Submit')