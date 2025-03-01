import os
import pytesseract
from PIL import Image

# Ruta de la carpeta con las imágenes JPG
image_folder = "nap_images"
output_txt = "result_nap.txt"

# Obtener lista de archivos JPG ordenados
image_files = sorted([f for f in os.listdir(image_folder) if f.endswith('.jpg')])

# Abrir archivo en modo escritura
with open(output_txt, "w", encoding="utf-8") as output_file:
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)

        # Cargar la imagen con PIL
        img = Image.open(image_path)

        # Convertir a escala de grises (opcional, mejora OCR en algunos casos)
        img = img.convert("L")

        # Extraer el texto con Tesseract
        text = pytesseract.image_to_string(img, lang="spa")

        # Escribir en el archivo con separación entre imágenes
        output_file.write(f"\n--- Texto extraído de {image_file} ---\n")
        output_file.write(text)
        output_file.write("\n\n")

print(f"Texto extraído y guardado en {output_txt}")
