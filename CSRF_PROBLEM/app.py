
from flask import Flask, request, render_template, make_response, redirect, url_for
import os
import hashlib
import base64
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.secret_key = os.urandom(32)
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")
ADMIN_2_FLAG = os.environ.get("ADMIN_2_FLAG")

users = {
    'guest': 'guest',
    'admin': ADMIN_PASSWORD,
    'admin_2': ADMIN_2_FLAG
}

session_storage = {}

def encrypt_username(username):
    return hashlib.sha256(username.encode()).hexdigest()

admin_2_csrf_token = base64.b64encode(os.urandom(16)).decode()

@app.route("/")
def index():
    session_id = request.cookies.get('sessionid', None)
    username = session_storage.get(session_id)

    if not username:
        return redirect(url_for('login')) 

    if username == "admin":
        return render_template('index_admin.html', text="자 이게 끝인 줄 알았죠!!? 아직 끝이 아닙니다!", username=username)
    
    if username == "admin_2":
        return render_template('index.html', text=f"FLAG: {ADMIN_2_FLAG}")
    
    return render_template('index.html', text=f"당연스럽게 guest에 로그인했겠지만, guest는 쓸모가 없어 친구 미안 😏")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        try:
            pw = users[username]
        except KeyError:
            return '<script>alert("User not found");history.go(-1);</script>'
        
        if pw == password:
            resp = make_response(redirect(url_for('index')))
            session_id = os.urandom(8).hex()
            session_storage[session_id] = username
            resp.set_cookie('sessionid', session_id)  
            
            if username == "admin_2":
                csrf_token = admin_2_csrf_token
            else:
                csrf_token = encrypt_username(username)
            
            resp.set_cookie('csrf_token', csrf_token)
            return resp

        return '<script>alert("Wrong password");history.go(-1);</script>'
    

@app.route("/change_password", methods=["POST"])
def change_password():
    pw = request.form.get("pw", "")  
    csrf_token = request.form.get("csrf_token", "") 
    target_user = request.form.get("username", "")  

    expected_csrf_token = encrypt_username(target_user)  

    if csrf_token != expected_csrf_token:
        return "Invalid CSRF token!", 403

    if target_user in users:
        users[target_user] = pw
        return f"{target_user}의 비밀번호 변경 완료!"
    else:
        return "User not found!", 404
    
@app.route("/flag", methods=["GET"])
def flag():
    session_id = request.cookies.get('sessionid', None)
    username = session_storage.get(session_id)

    if username != "admin":
        return """<script>alert("admin이 아니면 곤란해요!!"); history.go(-1);</script>""", 403

    print("/flag 엔드포인트에 요청 도착!")  

    pw = request.args.get("pw", "")  

    if "admin_2" in users:
        users["admin_2"] = pw  
        return "admin_2 비밀번호 변경 성공!", 200
        #return """<script>alert("성공!"); history.go(-1);</script>""", 200

    return "404.", 404
    #return """<script>alert("User not found!"); history.go(-1);</script>""", 404


@app.route("/vuln", methods=["GET"])
def vuln():
    session_id = request.cookies.get('sessionid', None)
    username = session_storage.get(session_id)

    if username != "admin":  
        return redirect(url_for('index'))
    
    param = request.args.get("param", "")

    if param == "":
        return render_template('vuln.html')

    xss_filter = ["frame", "script", "on", "img", "src"]
    for tag in xss_filter:
        param = param.replace(tag, "") 

    #print(f"최종 변환된 입력값: {param}")  디버깅용

    return param, 200, {'Content-Type': 'text/html'}  


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
