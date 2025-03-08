import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import logging
import os

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class OCRProcessor:
    def __init__(self, lang="eng"):
        """
        Inicializa el procesador OCR con el idioma especificado.
        
        :param lang: Código del idioma de Tesseract (por defecto, inglés 'eng').
                     Ejemplo: 'spa' para español, 'fra' para francés.
        """
        self.lang = lang

    def preprocess_image(self, image):
        """
        Aplica mejoras a la imagen para optimizar la precisión del OCR.
        :param image: Ruta de la imagen o un objeto PIL.Image.
        :return: Imagen procesada lista para OCR.
        """
        try:
            # Si es una ruta, abrir la imagen
            if isinstance(image, str):
                image = Image.open(image)

            # Convertir a escala de grises
            image = image.convert("L")

            # Aumentar contraste
            enhancer = ImageEnhance.Contrast(image)
            image = enhancer.enhance(3)

            # Reducir ruido con filtro
            image = image.filter(ImageFilter.MedianFilter(size=3))

            return image
        except Exception as e:
            logger.error(f"Error al procesar la imagen {image}: {e}")
            return None

    def extract_text(self, image_paths):
        """
        Extrae texto desde una o múltiples imágenes usando OCR.

        :param image_paths: Ruta de una imagen o lista de rutas de imágenes.
        :return: Texto extraído o diccionario con resultados de múltiples imágenes.
        """
        if isinstance(image_paths, str):
            image_paths = [image_paths]  # Convertir una única ruta en lista
        
        results = {}
        for image_path in image_paths:
            try:
                processed_image = self.preprocess_image(image_path)
                if processed_image is None:
                    results[image_path] = "Error al procesar la imagen."
                    continue

                text = pytesseract.image_to_string(processed_image, lang=self.lang)
                results[image_path] = text.strip()
            except Exception as e:
                logger.error(f"Error en OCR para {image_path}: {e}")
                results[image_path] = "Error en la extracción de texto."

        # Si solo hay una imagen, devolver solo el texto en vez de un diccionario
        return results if len(results) > 1 else list(results.values())[0]
    
    def recortar_texto(imagen_path, padding=10):
        # Cargar imagen
        imagen = cv2.imread(imagen_path)

        # Convertir a escala de grises
        gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

        # Aplicar umbral adaptativo para resaltar texto
        _, binaria = cv2.threshold(gris, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # Encontrar contornos
        contornos, _ = cv2.findContours(binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Crear una máscara para el área de texto
        x_min, y_min, x_max, y_max = imagen.shape[1], imagen.shape[0], 0, 0

        for contorno in contornos:
            x, y, w, h = cv2.boundingRect(contorno)
            if w > 30 and h > 30:  # Filtrar contornos pequeños
                x_min, y_min = min(x_min, x), min(y_min, y)
                x_max, y_max = max(x_max, x + w), max(y_max, y + h)

        # Agregar un pequeño padding alrededor del texto
        x_min, y_min = max(0, x_min - padding), max(0, y_min - padding)
        x_max, y_max = min(imagen.shape[1], x_max + padding), min(imagen.shape[0], y_max + padding)

        # Recortar la imagen
        imagen_recortada = imagen[y_min:y_max, x_min:x_max]

        return imagen_recortada

# Uso
imagen_procesada = recortar_tespoilerxto("ruta_a_tu_imagen.jpg")
cv2.imwrite("texto_recortado.jpg", imagen_procesada)
