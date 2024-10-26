from flask import  Flask,render_template
from datetime import  datetime

from flask_mail import Message

from .extensions import db,mail
from fl.config import ConfigInfo

from .utils.SendMail import sendMail1
#同级导入，需要用"."指定当前位置，发如是上级就直接导
from .forms.LoginForm import LoginForm
from .forms.UploadForm import UploadForm
from .models.Note import Note



app = Flask(__name__,static_url_path='/static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + ConfigInfo.MYSQL_USER + ':' \
                                        + ConfigInfo.MYSQL_PWD + '@' \
                                        + ConfigInfo.MYSQL_HOST + ':' \
                                        + ConfigInfo.MYSQL_PORT + '/' \
                                        + ConfigInfo.MYSQL_DB




#设置db的监听，设置Note.body实际上一些常用的，比如设置默认时间之类的
@db.event.listens_for(Note.body,'set')
def setNotEvent(target,value,old_value,initior):
    #value表示新给的值
        target.update_time = datetime.now()


#传参和删除
@app.route("/delete/<int:id>")
def deleteNote(id):
    note = Note.query.get(id)
    db.session.delete(note)
    db.session.commit()

    #比如查询id=10
    notes = Note.query.all()

    return  render_template("ch0501.html",notes=notes)


@app.route("/")
def index():
    notes = Note.query.all()

    new_note = Note(body='new add'+datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    #db.session.add(new_note)
    #db.session.commit()

    #比如查询id=10


    return  render_template("ch0501.html",notes=notes)

@app.route("/sendmail")
def sendMail():
    message = Message(recipients=['tttt9521@gmail.com'],subject='good',body='test '+datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    sendMail1(message)
    return  render_template("ch0501.html",)


def create_app(config):
    applicationApp = app

    applicationApp.config.from_object(config)

    db.init_app(app)
    mail.init_app(app)


    return applicationApp