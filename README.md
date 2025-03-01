# Proyecto de Extracción de Texto de Imágenes

Este proyecto utiliza `pytesseract` y `Pillow` para extraer texto de imágenes JPG en una carpeta específica y guardar el texto extraído en un archivo de texto.

## Requisitos

- Python 3.x
- Tesseract-OCR

## Instalación

1. Clona este repositorio.
2. Crea un entorno virtual:

    ```sh
    python -m venv venv
    ```

3. Activa el entorno virtual:

    - En Linux/MacOS:

        ```sh
        source venv/bin/activate
        ```

    - En Windows:

        ```sh
        .\venv\Scripts\activate
        ```

4. Instala las dependencias utilizando `pip`:

    ```sh
    pip install -r requirements.txt
    ```

5. Asegúrate de tener Tesseract-OCR instalado en tu sistema. Puedes descargarlo desde [aquí](https://github.com/tesseract-ocr/tesseract).

## Uso

1. Coloca las imágenes JPG en la carpeta `nap_images`.
2. Ejecuta el script [app.py](http://_vscodecontentref_/0):

    ```sh
    python app.py
    ```

3. El texto extraído se guardará en el archivo `result_nap.txt`.

## Licencia

Este proyecto está bajo la Licencia MIT.