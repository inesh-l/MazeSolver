from flask import Flask, request, render_template
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/'

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

