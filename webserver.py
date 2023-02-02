import os

from flask import Flask, render_template, request
import main

app = Flask(__name__)
UPLOAD_FOLDER = './static/uploads'


@app.route("/")
def homepage():
    return render_template('index.html')


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))


@app.route("/solved")
def solved():
    main.do()
    return render_template('solved.html')
