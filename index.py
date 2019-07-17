# http://flask.pocoo.org/docs/1.0/

from flask import Flask, url_for, render_template, jsonify, request
app = Flask(__name__)

# HOME PAGE
@app.route("/")
def home():
    return render_template('bookslot.html', posts=posts)

app.run()