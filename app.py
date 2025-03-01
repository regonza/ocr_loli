import os
import pytesseract
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
from threading import Thread

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
    
    messagebox.showinfo("Proceso completado", f"Texto extraído y guardado en {output_txt}")

def start_processing():
    folder_path = filedialog.askdirectory()
    if not folder_path:
        return
    
    output_txt = os.path.join(folder_path, "resultado.txt")
    btn_process.config(state=tk.DISABLED)
    lbl_status.config(text="Procesando...")
    
    def run():
        process_images(folder_path, output_txt)
        lbl_status.config(text="Proceso completado")
        btn_process.config(state=tk.NORMAL)
    
    Thread(target=run).start()

# Configurar la interfaz
tk_root = tk.Tk()
tk_root.title("OCR con Tesseract")
tk_root.geometry("400x200")

btn_process = tk.Button(tk_root, text="Seleccionar carpeta y procesar", command=start_processing)
btn_process.pack(pady=20)

lbl_status = tk.Label(tk_root, text="Listo")
lbl_status.pack(pady=10)

tk_root.mainloop()
