from flask_wtf import FlaskForm
from wtforms import Form,StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length,ValidationError



class LoginForm(FlaskForm):
    """
    ##  处理登录的表单,因为是flask-wtf,所以就要用FlaskForm
    """
    username = StringField('Username',validators=[DataRequired(message='用户名不能为空') ],render_kw={'placeholder':'input you username'})
    password = PasswordField('Password', validators=[DataRequired(),Length(6,message=u'密码最小6位')])
    submit = SubmitField('Log In')

    def validate_username(form,field):
        """

        :param field:  定义格式为"validate_属性名，而且需要加入form,field"两个参数
        :return:
        """
        if field.data != 'smith':
            raise  ValidationError(u'用户名必须是smith')