import os
from flask import Flask, flash, request, redirect, url_for
from flask import send_from_directory
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = '../temp/uploads/'

# only allow specific video file uploads
ALLOWED_EXTENSIONS = {'mp4'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            # saves the uploaded file in the temp folder
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    elif request.method == 'GET':
        # handle the file-get method
        # TODO: somehow replace this with our connect this to our current front-end
        #       as it stands, just opens on server-ip/index, need to try:
        #       return render_template('../frontend/index.html', title='Dashboard')
        return '''
            <!doctype html>
            <title>File Upload Test</title>
            <h1>Upload new File</h1>
            <form method=post enctype=multipart/form-data>
              <input type=file name=file>
              <input type=submit value=Upload>
            </form>
            '''
