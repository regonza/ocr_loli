FROM python:3.10

WORKDIR /app
COPY . /app

# Asegurar que Python encuentre los módulos correctamente
ENV PYTHONPATH=/app
ENV TESSDATA_PREFIX=/usr/share/tesseract-ocr/5/tessdata

RUN apt-get update && apt-get install -y tesseract-ocr tesseract-ocr-spa

RUN pip install --no-cache-dir -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
