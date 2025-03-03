import pytest
import pytesseract
import os
from PIL import Image, ImageDraw, ImageFont
from backend.services.ocr import OCRProcessor

@pytest.fixture
def ocr_processor():
    """Fixture que devuelve una instancia del OCRProcessor en español."""
    return OCRProcessor(lang="spa")

def create_test_image(text):
    """Genera una imagen en memoria con el texto dado."""
    img = Image.new("RGB", (300, 100), color="white")
    draw = ImageDraw.Draw(img)

    # Verificar si arial.ttf está disponible en Linux, si no usar una fuente alternativa
    font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Fuente segura en Linux
    if not os.path.exists(font_path):
        font = None  # Si no está disponible, dejar que PIL use la predeterminada
    else:
        font = ImageFont.truetype(font_path, 24)

    draw.text((10, 40), text, fill="black", font=font)
    return img

def test_ocr_generated_image(ocr_processor):
    """Prueba OCR con una imagen generada en memoria con texto visible."""
    img = create_test_image("Hola Mundo")
    texto_extraido = pytesseract.image_to_string(img, lang="spa")

    assert isinstance(texto_extraido, str)
    assert "Hola Mundo" in texto_extraido  # Asegura que el OCR reconoce el texto

def test_ocr_blank_image(ocr_processor):
    """Prueba OCR con una imagen completamente en blanco (sin texto)."""
    img = Image.new("RGB", (300, 100), color="white")  # Imagen sin texto
    texto_extraido = pytesseract.image_to_string(img, lang="spa")

    assert texto_extraido.strip() == ""  # OCR no debe detectar texto

def test_ocr_invalid_image(ocr_processor):
    """Prueba el manejo de error con una imagen no válida."""
    resultado = ocr_processor.extract_text("invalid_file.txt")
    assert resultado == "Error al procesar la imagen."

def test_ocr_multiple_images(ocr_processor):
    """Prueba OCR con múltiples imágenes generadas en memoria."""
    img1 = create_test_image("Texto 1")
    img2 = create_test_image("Texto 2")

    texto1 = pytesseract.image_to_string(img1, lang="spa").strip()
    texto2 = pytesseract.image_to_string(img2, lang="spa").strip()

    assert isinstance(texto1, str)
    assert isinstance(texto2, str)
    
    # Tolerar pequeñas diferencias
    assert "Texto" in texto1
    assert "Texto" in texto2

def test_ocr_preprocessing(ocr_processor):
    """Prueba que el preprocesamiento de imagen no falle."""
    img = create_test_image("Test Preprocesado")
    processed_img = ocr_processor.preprocess_image(img)

    assert processed_img is not None  # La imagen debe ser procesada sin errores
    assert isinstance(processed_img, Image.Image)  # Debe seguir siendo un objeto PIL