from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, DateTimeField
from wtforms.validators import DataRequired

class LogEntryForm(FlaskForm):
    child_name = StringField('Child Name', validators=[DataRequired()])
    category = SelectField('Category', choices=[
        ('daily_activity', 'Daily Activity'),
        ('medication', 'Medication'),
        ('behavior', 'Behavior'),
        ('education', 'Education'),
        ('other', 'Other')
    ], validators=[DataRequired()])
    timestamp = DateTimeField('Date and Time', format='%Y-%m-%d %H:%M', validators=[DataRequired()])
    content = TextAreaField('Log Content', validators=[DataRequired()])
    submit = SubmitField('Submit Log')