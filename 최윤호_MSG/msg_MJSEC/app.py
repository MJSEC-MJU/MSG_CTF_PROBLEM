from flask import Flask, request,render_template, render_template_string

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/amir")
def greet():
    add = request.args.get("address", "")
    template = f"이 주소는, { add }에요!"
    blacklist = ["str","object","Popen","config", "os"]
    
    if any(keyword in add for keyword in blacklist):
        return "삐삑.. 여긴 아닌것 같아요.. ", 400

    return render_template_string(template)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)