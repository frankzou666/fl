from flask import  Flask,render_template,request,redirect,url_for

#同级导入，需要用"."指定当前位置，发如是上级就直接导
from .forms.LoginForm import LoginForm
from .forms.UploadForm import UploadForm


app = Flask(__name__,static_url_path='/static')


@app.route("/movie",)
def getMovies():


    return  render_template("movie.html",)

@app.route("/")
def index():
    return  render_template("index.html")

@app.route("/form01",methods=['GET','POST'])
def form01():
    #实例化form,并带给页面
    loginForm = LoginForm()
    if   loginForm.validate_on_submit() and request.method=='POST':
        return render_template('index.html')
    return  render_template("form01.html",loginForm=loginForm)

@app.route("/upload",methods=['GET','POST'])
def upload():
    uploadFrom=UploadForm()
    if uploadFrom.validate_on_submit():
        # 帮我们处理好了文件，直接通过字段属性.data就可以获取到了
        f = uploadFrom.uploadFile.data
        f.save('/upload')
        return redirect(url_for('index'))
    return  render_template("upload.html",uploadFrom=uploadFrom)


def create_app(config):
    applicationApp = app
    applicationApp.config.from_object(config)
    return applicationApp