# 📝 Textter - OCR & Transcripción de Audio 🇦🇷 🚀

> **Un proyecto desarrollado con amor y código por Cota & NachoGPT 🤖💙**

## 🤔 ¿Qué es Textter?

Textter es **la posta** para extraer texto de imágenes y audios, sin depender de la nube y sin gastar un mango. Todo funciona localmente, como debe ser. 💪

Si necesitás digitalizar texto de imágenes o transcribir audios sin complicaciones, este proyecto te va a encantar. Además, está pensado para ser modular, escalable y fácil de mejorar.

---

## 🎯 Características Principales

✅ **OCR con Tesseract**: Extraé texto de imágenes 📷📝  
✅ **Transcripción de Audio con WhisperX** 🎙️➡️📝  
✅ **Procesamiento de Texto con LangGraph** 🤖  
✅ **100% local y sin costos** 💸🚫  
✅ **API con FastAPI** 🚀  
✅ **Frontend moderno (Next.js / SvelteKit)** 🎨  
✅ **Testeado al 100% con Pytest y GitHub Actions** ✅  
✅ **Docker para que corra en cualquier lado** 🐳  

---

## ⚙️ Tecnologías Utilizadas

### 🖥️ Backend
- **FastAPI** → Rápido y moderno.
- **pytesseract** → Para el OCR.
- **whisperx** → Para la transcripción de audio.
- **LangGraph** → Procesamiento del texto extraído.
- **SQLite (opcional)** → Para almacenar historial.

### 🎨 Frontend
- **React con Next.js** o **SvelteKit** (vos elegís el mejor stack para vos 👀).

### 🐳 Infraestructura
- **Docker** → Para que levante sin dramas.
- **GitHub Actions** → Para correr los tests antes de cada merge.

---

## 📦 Instalación & Setup

### 🏗️ Requisitos Previos
Antes de empezar, asegurate de tener instalado:

✅ **Python 3.10+** 🐍
✅ **Tesseract OCR** 🧐 (`tesseract --version` para chequear)
✅ **pip** (gestor de paquetes de Python)
✅ **Docker (opcional, pero recomendado)** 🐳

### 🔧 Instalación (Backend & OCR)
```bash
# Cloná el repo
$ git clone https://github.com/tuusuario/textter.git
$ cd textter

# Creá y activá un entorno virtual (recomendado)
$ python -m venv venv
$ source venv/bin/activate  # Linux/macOS
$ venv\Scripts\activate  # Windows

# Instalá las dependencias
$ pip install -r backend/requirements.txt
```

### 📸 Configuración de Tesseract OCR
Si usás Windows, asegurate de configurar el path en `ocr.py`:
```python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
```
Para Linux/macOS, basta con instalarlo:
```bash
sudo apt install tesseract-ocr  # Ubuntu/Debian
brew install tesseract  # macOS
```

### 🏃 Levantar el Backend
```bash
$ uvicorn backend.main:app --reload
```
Abrí tu navegador y entrá a `http://127.0.0.1:8000/docs` para ver la documentación automática de FastAPI.

### 🎭 Frontend (si lo querés usar)
```bash
$ cd frontend
$ npm install
$ npm run dev
```
Abrí `http://localhost:3000` en el navegador y disfrutá. 🎉

---

## ✅ Testing
Acá testeamos todo, papá.  

### 🧪 Ejecutar Tests Unitarios
```bash
pytest --cov=backend
```
Esto ejecuta **todos los tests** y te muestra el porcentaje de cobertura.

### 🔄 Automatización con GitHub Actions
Cada vez que hagas un push, GitHub correrá los tests automáticamente.  
Si querés probarlo manualmente, corré:
```bash
git push origin tu_rama
```

---

## 🎉 Contribuir
Si tenés una idea loca o querés mejorar algo, ¡mandá un PR! 🙌

1. Forkeá el repo 🍴
2. Creá una branch nueva: `git checkout -b feature-nueva`
3. Codeá como un campeón 🏆
4. Asegurate de que los tests pasen ✅
5. Hacé commit siguiendo el formato de **commitizen** 🎭
6. Mandá el PR y esperá nuestra review con mate en mano ☕

---

## 📜 Licencia
Este proyecto está bajo la licencia **MIT**. Usalo, modificalo y compartilo libremente. 😎

---

🚀 **Cota & NachoGPT** - Código, mate y pasión. 🇦🇷💻