
from fl.extensions import db
class Note(db.Model):
    #自定义表名，且同时为我们定义了一构造器
    __tablename__= 'note'
    id = db.Column(db.Integer,primary_key=True)
    body = db.Column(db.String)
    update_time = db.Column(db.Date)