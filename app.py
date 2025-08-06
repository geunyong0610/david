from flask import Flask, render_template 
import socket

app = Flask(__name__)

@app.route("/")
def home():
    if app.debug:
        hostname = '컴퓨터(인스턴스)' + socket.gethostname()
    else:
        hostname = ' '
    
    return render_template("index.html", computername=hostname) # 사용자가 /menu로 접속시 Flask가 이 파일 찾아서 내용 읽고 html형태로 브라우저한테 보내줌

@app.route("/test1")
def test1():
    return render_template('test1.html')
   
if __name__ == '__main__':
    app.run('0.0.0.0', 80, debug=True)#Flask가 개발자를 위해 자동 리로드+ 상세오류페이지 제공(Flask자체의 디버깅 기능 