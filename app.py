import os
import predict as pdt
import config as cfg
from flask import Flask, request, redirect, url_for, render_template
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename

# Setting up environment
if not os.path.isdir(cfg.OUTPUT):
    print('Creating folder..')
    os.mkdir(cfg.OUTPUT)

app = Flask(__name__)
Bootstrap(app)
app.config['UPLOAD'] = cfg.OUTPUT


@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        # Checking if the post request has file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        # Checking if no file was submitted to HTML form
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file and pdt.allow_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD'], filename))
            output = pdt.make_prediction(filename)
            path_img = url_for('static', filename=filename)
            result = {
                'output': output,
                'path_to_image': path_img,
                'size': cfg.SIZE
            }
            return render_template('show.html', result=result)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
