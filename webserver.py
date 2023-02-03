import os

from flask import Flask, render_template, request, redirect
import main

app = Flask(__name__)
UPLOAD_FOLDER = '/static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def homepage():
    return render_template('index.html')


@app.route("/solve", methods=['GET', 'POST'])
def solved():
    if request.method == 'POST':
        f = request.files['maze']
        f.save('./static/uploads/maze.png')
        startX = request.form['startX']
        startY = request.form['startY']
        endX = request.form['endX']
        endY = request.form['endY']
        main.do_modified(startX, startY, endX, endY)
        return redirect('/solved')


@app.route("/solved")
def show():
    return render_template('solved.html')