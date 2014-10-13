import google
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
@app.route("/index",methods=["GET","POST"])
def index():
	if request.method=="GET":
		return render_template("index.html")
	else:
		button = request.form['s']
		if button == "search":
			return render_template("result.html", result="searched")
			print "here"
		if button == "lucky":
			return render_template("result.html",result="lucky")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/result")
def result():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)
