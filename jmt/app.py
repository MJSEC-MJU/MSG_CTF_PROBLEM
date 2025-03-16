from flask import Flask, request, redirect, render_template, make_response, abort
import jwt
import hashlib
import hmac
import datetime
from cryptography.hazmat.primitives import serialization

app = Flask(__name__)

def read_file(file_path):
    try:
        with open(file_path, 'r') as f:
            return f.read().strip()
    except Exception as e:
        print(e)
        exit(1)

def read_pubkey_der(file_path):
    try:
        with open(file_path, 'rb') as f:
            pubkey_pem = f.read()
            public_key = serialization.load_pem_public_key(pubkey_pem)
            pubkey_der = public_key.public_bytes(
                encoding=serialization.Encoding.DER,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
            return pubkey_der
    except Exception as e:
        print(e)
        exit(1)

FLAG = read_file('/flag')
priv_key = read_file('/priv.pem')
pub_key = read_file('/pub.crt')
pub_key_der = read_pubkey_der('/pub.crt')

accounts = {
    'admin': {'password': FLAG},
    'guest': {'password': 'guest'}
}

def verify_token(token):
    try:
        header = jwt.get_unverified_header(token)
        alg = header.get('alg')
        if alg == 'RS256':
            return jwt.decode(token, pub_key, algorithms=['RS256'])
        elif alg == 'HS256':
            return jwt.decode(token, pub_key_der, algorithms=['HS256'])
        elif alg == 'ES256':
            return jwt.decode(token, pub_key, algorithms=['ES256'])
        else:
            return None
    except Exception:
        return None

def create_account_token(username):
    payload = {
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    token = jwt.encode(payload, priv_key, algorithm='RS256')
    return token

def is_admin(token):
    data = verify_token(token)
    if data and data.get('username') == 'admin':
        return True
    return False

def require_authentication(func):
    def wrapper(*args, **kwargs):
        token = request.cookies.get('token')
        if not token or verify_token(token) is None:
            return redirect('/login')
        return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper

@app.route('/login', methods=['GET'])
def login_get():
    token = request.cookies.get('token')
    if token and verify_token(token) is not None:
        return redirect('/')
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    token = request.cookies.get('token')
    if token and verify_token(token) is not None:
        return "you are already logged in.", 403

    username = request.form.get('username')
    password = request.form.get('password')

    if not username or not password:
        return "username or password is empty.", 400

    if username not in accounts:
        return "username or password is wrong.", 401

    provided_password_hash = hashlib.sha256(password.encode()).hexdigest()
    stored_password_hash = hashlib.sha256(accounts[username]['password'].encode()).hexdigest()
    if not hmac.compare_digest(provided_password_hash, stored_password_hash):
        return "username or password is wrong.", 401

    token = create_account_token(username)
    response = make_response(redirect('/'))
    response.set_cookie('token', token, httponly=True)
    return response

@app.route('/logout', methods=['POST'])
def logout():
    response = make_response(redirect('/login'))
    response.delete_cookie('token')
    return response

@app.route('/admin', methods=['GET'])
def admin():
    token = request.cookies.get('token')
    if not token or not is_admin(token):
        abort(404)
    return FLAG

@app.route('/', methods=['GET'])
@require_authentication
def index():
    token = request.cookies.get('token')
    user_data = verify_token(token)
    username = user_data.get('username')
    is_admin_val = is_admin(token)

    return render_template(
        'index.html',
        isAdmin=is_admin_val,
        username=username,
        flag=FLAG if is_admin_val else None
    )
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)
