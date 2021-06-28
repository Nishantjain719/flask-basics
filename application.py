from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    names = ['elon', 'bob', 'alise']
    return render_template("index.html", names=names)


@app.route("/more")
def more():
    return render_template("more.html")


@app.route("/hello", methods=["GET","POST"])
def hello():
    if request.method == "GET":
        return "Please submit the form instead"
    else:
        name = request.form.get("name")
        # passing in name as var in template and getting it from form which user just filed out
        return render_template("hello.html", name=name)
