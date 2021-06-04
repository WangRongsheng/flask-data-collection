
from werkzeug.utils import secure_filename
from flask import Flask, render_template, jsonify, request, make_response, send_from_directory, abort
import time
import os
import base64
 
app = Flask(__name__)
UPLOAD_FOLDER = 'upload'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'zip', 'JPG', 'PNG', 'gif', 'GIF', 'ZIP'])
 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
 
@app.route('/')
def upload_test():
    return render_template('index.html')
 
# 上传文件
@app.route('/index', methods=['POST'], strict_slashes=False)
def api_upload():
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    f = request.files['photo']
    n = request.form['name']

    if f and allowed_file(f.filename):
        fname = secure_filename(f.filename)
        print(fname)
        #ext = fname.rsplit('.', 1)[1]
        #new_filename = Pic_str().create_uuid() + '.' + ext
        dirs = file_dir +'/' + str(n)
        if not os.path.exists(dirs):
            os.makedirs(dirs)
        f.save(os.path.join(dirs, fname)) #new_filename
        return "文件上传成功!!"
        #return jsonify({"success": 0, "msg": "success"})
    #else:
        #return jsonify({"error": 1001, "msg": "error"})
    #return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
    #app.run('0.0.0.0', 5000)