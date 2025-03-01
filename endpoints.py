from flask import Flask, request, render_template, send_file
import os
import pytesseract
from PIL import Image
import zipfile

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "results"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

def process_images(folder_path, output_txt):
    image_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.jpg')])
    
    with open(output_txt, "w", encoding="utf-8") as output_file:
        for image_file in image_files:
            image_path = os.path.join(folder_path, image_file)
            img = Image.open(image_path).convert("L")
            text = pytesseract.image_to_string(img, lang="spa")
            output_file.write(f"\n--- Texto extraído de {image_file} ---\n")
            output_file.write(text)
            output_file.write("\n\n")

def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file uploaded", 400
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400
    
    zip_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(zip_path)
    extract_folder = os.path.join(UPLOAD_FOLDER, os.path.splitext(file.filename)[0])
    os.makedirs(extract_folder, exist_ok=True)
    extract_zip(zip_path, extract_folder)
    
    output_txt = os.path.join(RESULT_FOLDER, "resultado.txt")
    process_images(extract_folder, output_txt)
    
    return send_file(output_txt, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
