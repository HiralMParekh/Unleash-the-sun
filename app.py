from flask import Flask, request, render_template, redirect, url_for
from flask import *

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data.html')
def data():
    return render_template('data.html')
    
    
@app.route('/photos.html')
def photos():
    return render_template('photos.html')
    

@app.route('/upload', methods=['POST'])
def upload_file():
    return render_template('app1.py')

if __name__ == '__main__':
    app.run(debug=True)
    
from flask import Flask, render_template
 
app = Flask(_name_)
 
@app.route('/')
def home():
    return render_template('image_render.html')
 
if _name_ == '_main_':
    app.run(debug=True, port=9000)

    