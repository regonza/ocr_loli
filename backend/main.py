from fastapi import FastAPI, File, UploadFile
from services.ocr import OCRProcessor
import shutil
import os

app = FastAPI()

ocr_processor = OCRProcessor(lang="spa")

@app.post("/ocr/")
async def process_ocr(file: UploadFile = File(...)):
    """
    Recibe una imagen, la guarda temporalmente y devuelve el texto extraído.
    """
    temp_path = f"temp_{file.filename}"
    
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    texto = ocr_processor.extract_text(temp_path)

    os.remove(temp_path)  # Eliminar el archivo temporal

    return {"text": texto}