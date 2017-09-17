from wtforms import Form, StringField, PasswordField, SubmitField, validators


class RegisterFormContent(Form):
    mobile = StringField('mobile', [validators.Length(min=7, max=11)])
    password = PasswordField('New Password', [validators.DataRequired(), validators.EqualTo('confirm', message='Passwords must match')])
    password_repeat = PasswordField('Repeat Password')
    mobile_code = StringField('I accept the TOS', [validators.DataRequired()])
    submit = SubmitField('Submit')
