from flask import Flask, request, render_template, redirect, url_for
import os
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        print(os.path.splitext('static/uploads/'+f.filename))

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

