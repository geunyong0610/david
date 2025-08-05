from flask import Flask, request, Response, render_template 
import socket
import os
from io import BytesIO
from gtts import gTTS


DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'ko')
app = Flask(__name__)

@app.route("/")
def home():

    text = "Hello, DevOps"

    lang = request.args.get('lang', DEFAULT_LANG)
    fp = BytesIO()
    gTTS(text, "com", lang).write_to_fp(fp)

    return Response(fp.getvalue(), mimetype='audio/mpeg') # 페이지 전달없이 바로 재생

@app.route("/menu")
def menu():
    if app.debug:
        hostname = '컴퓨터(인스턴스)' + socket.gethostname()
    else:
        hostname = ' '
    

    return render_template("menu.html", computername=hostname) # 사용자가 /menu로 접속시 Flask가 이 파일 찾아서 내용 읽고 html형태로 브라우저한테 보내줌

@app.route("/test1")
def test1():
    return render_template('test1.html')


    
if __name__ == '__main__':
    app.run('0.0.0.0', 80, debug=True)#Flask가 개발자를 위해 자동 리로드+ 상세오류페이지 제공(Flask자체의 디버깅 기능 
