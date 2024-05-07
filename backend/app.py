import os
from flask import Flask, flash, request, redirect, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename
from src.run import run

UPLOAD_FOLDER = '../temp/uploads/'
ALLOWED_EXTENSIONS = {'mp4'}

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploadVideo', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        return jsonify({'message': run(os.path.join(app.config['UPLOAD_FOLDER'], filename), app)}), 200
    else:

        return jsonify({'message': 'File upload failed'}), 400

