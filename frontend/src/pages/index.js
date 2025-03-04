import { useState } from "react";
import UploadAnimation from "../components/UploadAnimation";
import '../app/globals.css'; // ✅ Importación sin alias para evitar errores


export default function Home() {
  const [files, setFiles] = useState([]);
  const [texts, setTexts] = useState({});
  const [loading, setLoading] = useState(false);

  const handleFileSelection = (selectedFiles) => {
    setFiles(selectedFiles);
  };

  const handleUpload = async () => {
    const API_URL =
      typeof window !== "undefined"
        ? "http://localhost:8000/ocr/"
        : "http://backend:8000/ocr/";

    if (files.length === 0) {
      alert("Selecciona al menos una imagen.");
      return;
    }

    setLoading(true);
    const newTexts = {};

    for (const file of files) {
      const formData = new FormData();
      formData.append("file", file);

      try {
        const response = await fetch(API_URL, {
          method: "POST",
          body: formData,
        });
        const data = await response.json();
        newTexts[file.name] = data.text;
      } catch (error) {
        console.error("Error:", error);
        newTexts[file.name] = "❌ Error al procesar la imagen";
      }
    }

    setTexts(newTexts);
    setLoading(false);
  };

  return (
    <div className="">
      <h1 className="">
        <span>🔍</span> OCR - Subí una o varias imágenes
      </h1>

      {/* Componente de carga animado */}
      <UploadAnimation onFilesSelected={handleFileSelection} />

      <button
        onClick={handleUpload}
        className=""
        disabled={loading}
      >
        {loading ? "Procesando..." : "Extraer Texto"}
      </button>

      {/* Vista previa de imágenes */}
      <div className="mt-6 grid grid-cols-1 md:grid-cols-2 gap-6">
        {files.map((file) => (
          <div key={file.name} className="bg-white p-6 rounded-xl shadow-lg">
            <img
              src={URL.createObjectURL(file)}
              alt={file.name}
              className="w-full h-40 object-cover rounded mb-4"
            />
            <p className="text-lg font-semibold">{file.name}</p>
            <p className="text-gray-600">{texts[file.name] || "⏳ Procesando..."}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
