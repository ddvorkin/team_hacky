import google, re, datasearch
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
@app.route("/index",methods=["GET","POST"])
def index():
	if request.method=="GET":
		return render_template("index.html")
	else:
		button = request.form['s']
		query = request.form['search']
                output = ""
		if re.search("when", query, re.I) != None:
			output = datasearch.search_date(query)
		if re.search("who", query, re.I) != None:
			output = datasearch.search_who(query)
		if re.search("where", query, re.I) != None:
			output = datasearch.search_where(query)

        if button == "search" and output == "":
            return render_template("index.html",result=output)
        if button == "search" and output != "":
            return render_template("index.html", link_list=datasearch.search_list(query))
        if button == "lucky":
            return render_template("index.html",result=output)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/result")
def result():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)
