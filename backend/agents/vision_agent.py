import os
import base64
import ollama
from langgraph.graph import StateGraph
from langchain_ollama import ChatOllama
from pydantic import BaseModel

# 🔹 Configuración de modelos
llm_text = ChatOllama(model="llama3.2:latest")
vision_model = "granite3.2-vision"

# 🔹 Definición del esquema de estado
class AgentState(BaseModel):
    image_path: str
    ocr_tradicional: str = ""
    ocr_vision: str = ""
    fusion_texto: str = ""

# 🔹 Tool: OCR Tradicional
def ocr_tool(image_path: str) -> str:
    import pytesseract
    from PIL import Image
    texto = pytesseract.image_to_string(Image.open(image_path))

    # 🔥 Guardar resultado OCR en archivo separado
    nombre_archivo = os.path.basename(image_path).replace(".", "_")
    archivo_ocr = f"img_ocr_{nombre_archivo}.txt"
    with open(archivo_ocr, "w", encoding="utf-8") as f:
        f.write(texto)

    print(f"✅ Resultado OCR guardado en: {archivo_ocr}")
    return texto

# 🔹 Tool: OCR con Granite3.2-Vision usando Ollama
def vision_ocr(image_path: str) -> str:
    # 🔥 Estructurar correctamente el prompt
    prompt = "Extrae el texto de la imagen directamente sin agregar comentarios ni respuestas adicionales."

    # 🔥 Enviar el prompt y la imagen directamente a Ollama
    response = ollama.chat(
        model=vision_model,
        messages=[
            {
                "role": "user",
                "content": prompt,
                "images": [image_path]  # 🔥 Pasar la ruta de la imagen directamente
            }
        ]
    )

    # 🔎 Extraer el contenido del mensaje
    texto = response['message']['content']

    # 🔥 Guardar resultado en archivo separado
    nombre_archivo = os.path.basename(image_path).replace(".", "_")
    archivo_vision = f"img_granite_{nombre_archivo}.txt"
    with open(archivo_vision, "w", encoding="utf-8") as f:
        f.write(texto)

    print(f"✅ Resultado Granite3.2 guardado en: {archivo_vision}")
    return texto


# 🔹 Función para procesar ambos OCRs al mismo tiempo
def entrada_ocr(state: AgentState) -> AgentState:
    state.ocr_tradicional = ocr_tool(state.image_path)
    state.ocr_vision = vision_ocr(state.image_path)
    return state

# 🔹 Función para fusionar textos de una imagen
def fusionar_texto(state: AgentState) -> AgentState:
    prompt = f"""
    Corrige y combina el siguiente texto de una imagen escaneada.  
    NO agregues comentarios o respuestas dirigidas al usuario.  
    Devuelve solo el texto corregido y estructurado.  

    Texto OCR Tradicional:
    {state.ocr_tradicional}

    Texto del Modelo de Visión:
    {state.ocr_vision}

    Devuelve solo el texto final, sin agregar ningún comentario o explicación.
    """
    
    response = llm_text.invoke(prompt)
    texto_corregido = response.content.strip()

    # 🔎 Limpieza de texto irrelevante usando regex
    import re
    texto_corregido = re.sub(r'^(¡?[A-Z][a-z]+[,.!:]?\s*)+', '', texto_corregido)  # Eliminar saludos
    texto_corregido = re.sub(r'Espero que.*preguntar\.?$', '', texto_corregido, flags=re.MULTILINE)  # Eliminar comentarios
    texto_corregido = re.sub(r'El texto corregido presenta.*', '', texto_corregido, flags=re.MULTILINE)  # Eliminar explicaciones
    texto_corregido = re.sub(r'\n\s*\n', '\n', texto_corregido).strip()  # Eliminar líneas vacías extra

    state.fusion_texto = texto_corregido

    return state

# 🔹 Pipeline de LangGraph
def build_graph():
    builder = StateGraph(
        state_schema=AgentState
    )

    # Nodos del grafo
    builder.add_node("entrada_ocr", entrada_ocr)
    builder.add_node("fusion_texto_node", fusionar_texto)

    # Conexiones
    builder.set_entry_point("entrada_ocr")
    builder.add_edge("entrada_ocr", "fusion_texto_node")

    return builder.compile()

# 🔹 Procesamiento de carpeta y generación de documento
def procesar_carpeta(carpeta: str, salida: str):
    graph = build_graph()
    textos_procesados = []  

    for imagen in sorted(os.listdir(carpeta)):
        if imagen.endswith((".png", ".jpg", ".jpeg", ".tiff")):
            ruta = os.path.join(carpeta, imagen)
            state = AgentState(image_path=ruta)
            
            # ✅ Ejecutar de forma independiente y guardar directamente el resultado
            output = graph.invoke(state)
            fusion_texto = output.get("fusion_texto", "")
            
            if fusion_texto:
                # ✅ Añadir el resultado a la lista
                textos_procesados.append(fusion_texto.strip())

    # 🔹 Concatenación con separadores entre páginas
    documento_final = "\n\n--- Página siguiente ---\n\n".join(textos_procesados)

    # 🔹 Guardar en un archivo de salida
    with open(salida, "w", encoding="utf-8") as f:
        f.write(documento_final)

    print(f"✅ Documento final guardado en: {salida}")


# 🔹 Uso del procesamiento
carpeta_imagenes = "/home/cota/Documents/Code/ocr_loli/input_images"
archivo_salida = "documento_final.txt"
procesar_carpeta(carpeta_imagenes, archivo_salida)