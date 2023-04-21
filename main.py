import os

from flask import Flask, render_template, request

from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads/'

Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def upload_file():
    return "Hello world"


@app.route('/uploader', methods=['GET', 'POST'])
def process_file():
    if request.method == 'POST':
        f = request.files['file']
        s_secure_filename = secure_filename(f.filename)
        # if s_secure_filename.endswith('.csv'):
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], s_secure_filename))
        return 'file processed successfully'


if __name__ == "__main__":
    app.run(debug=True)
