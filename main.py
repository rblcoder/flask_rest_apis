import os

from flask import Flask, render_template, request
import requests
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = '/home/ch1/Documents/uploads/'

Headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def upload_file():
    return render_template('upload.html')


@app.route('/uploader', methods=['GET', 'POST'])
def process_file():

    if request.method == 'POST':
        f = request.files['file']
        s_secure_filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], s_secure_filename))
        return 'file processed successfully'


if __name__ == "__main__":
    app.run(debug=True)
