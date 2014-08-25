import os
from flask import Flask
from flask import render_template
from flask import request
from page_one import app_one
from page_two import app_two


app = Flask(__name__)
app.register_blueprint(app_one)
app.register_blueprint(app_two)


#Create our index or root / route
@app.route("/")
@app.route("/index")
def index():
	name = 'Guest'
	return render_template('index.html', name=name)


if __name__ == "__main__":
	app.run(debug = "True")
