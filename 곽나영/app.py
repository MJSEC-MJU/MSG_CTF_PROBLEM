from flask import Flask, request, render_template, redirect, url_for, session
import pymysql
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

DB_HOST = os.environ["DB_HOST"]
DB_PORT = int(os.environ["DB_PORT"])
DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_NAME = os.environ["DB_NAME"]


def get_db_connection():
    return pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )


# 기본 페이지 라우터
@app.route("/", methods=["GET"])
def index():
    if "logged_in" in session:
        uid = session["uid"]
        if uid == "admin":
            return render_template("index.html", flag=True)
        else:
            return render_template(
                "index.html", flag=False, message="admin이 아닙니다."
            )
    else:
        return render_template(
            "index.html", message="로그인 해주세요.", login_button=True
        )


# 로그인 처리 라우터
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uid = request.form.get("uid")
        password = request.form.get("password")
        if uid and password:
            try:
                conn = get_db_connection()
                cur = conn.cursor()

                query = f"SELECT * FROM test_table WHERE uid='{uid}' AND upassword='{password}';"
                cur.execute(query)
                user = cur.fetchone()
                conn.close()
                if user:
                    session["logged_in"] = True

                    session["uid"] = user["uid"]
                    return redirect(url_for("index"))
                else:
                    return render_template(
                        "login.html", error="잘못된 아이디 또는 비밀번호입니다."
                    )
            except Exception as e:
                return f"SQL 오류 발생: {str(e)}"
        else:
            return render_template(
                "login.html", error="아이디와 비밀번호를 입력하세요."
            )
    else:
        return render_template("login.html")


# 로그아웃 라우터
@app.route("/logout", methods=["GET"])
def logout():
    session.pop("logged_in", None)
    session.pop("uid", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
