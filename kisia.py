from flask import Flask, render_template, request
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route('/file_upload', methods = ['GET', 'POST'])
def file_upload():
    if request.method == 'POST':
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return '파일 저장됨'
    else:
        return render_template('file_upload.html')
    
if __name__ == '__main__':
    app.run(port=5000, debug=True)
