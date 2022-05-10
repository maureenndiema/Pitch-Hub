from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import InputRequired

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Write a brief bio about you.',validators = [InputRequired()])
    submit = SubmitField('Save')

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    post = TextAreaField('Pitch', validators=[InputRequired()])
    category = SelectField('Category', choices=[('ART', 'ART'), ('MUSIC', 'MUSIC'), ('POETRY', 'POETRY')],validators=[InputRequired()])
    submit = SubmitField('Pitch')


class CommentForm(FlaskForm):
    comment = TextAreaField('Comment Here', validators=[InputRequired()])
    submit = SubmitField('Comment')