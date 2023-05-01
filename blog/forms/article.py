import wtforms
from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, TextAreaField, SelectMultipleField


class ArticleAddForm(FlaskForm):
    title = StringField('Title', [validators.DataRequired()])
    text = TextAreaField('Text', [validators.DataRequired()])
    tags = SelectMultipleField('Tags', coerce=int)
    submit = SubmitField('Add')
