from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about you.',validators = [Required()])
    submit = SubmitField('Save')

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    post = TextAreaField('Pitch', validators=[Required()])
    category = SelectField('Category', choices=[('ART', 'ART'), ('MUSIC', 'MUSIC'), ('POETRY', 'POETRY')],validators=[Required()])
    submit = SubmitField('Pitch')


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment Here', validators=[Required()])
    submit = SubmitField('Comment')