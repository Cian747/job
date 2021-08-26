from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField, FileField
from wtforms.validators import Required
from wtforms import ValidationError


# class BlogForm(FlaskForm):

#  title = StringField('Blog title',validators=[Required()])

#  author = StringField('Name',validators=[Required()])

#  review = TextAreaField('Write blog here: ')

#  submit = SubmitField('Submit')



class UpdateProfile(FlaskForm):
    profile_pic_path= FileField('Update your profile pic')
    submit = SubmitField('Submit')


class UpdateBio(FlaskForm):
    bio = TextAreaField('Bio',validators = [Required()])
    # submit = SubmitField('Submit')
