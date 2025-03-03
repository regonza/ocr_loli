from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from services.ocr import OCRProcessor
import shutil
import os




app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir cualquier origen (modificar para producción)
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los headers
)

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