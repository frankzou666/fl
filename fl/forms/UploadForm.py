from flask_wtf import FlaskForm
from wtforms import Form,StringField,PasswordField,BooleanField,SubmitField,FileField
from wtforms.validators import DataRequired,Length,ValidationError

class UploadForm(FlaskForm):
    uploadFile = FileField()
    submit = SubmitField(u'上传')