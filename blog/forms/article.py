from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField


class ArticleAddForm(FlaskForm):
    title = StringField('Title', [validators.DataRequired()])
    text = StringField('Text', [validators.DataRequired()])
    submit = SubmitField('Add')
