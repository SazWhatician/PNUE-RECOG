import os
from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename
from model_logic import predict_pneumonia

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def upload():
    if 'file' not in request.files: return "No file"
    file = request.files['file']
    if file.filename == '': return "No filename"
    
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    
    result, confidence = predict_pneumonia(filepath)
    
    return render_template('predict.html', 
                           result=result, 
                           confidence=confidence, 
                           filename=filename)

if __name__ == '__main__':
    app.run(debug=True)