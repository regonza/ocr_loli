import { useState } from "react";

export default function Home() {
  const [files, setFiles] = useState([]); // Lista de imágenes seleccionadas
  const [texts, setTexts] = useState({}); // Almacena el texto de cada imagen
  const [loading, setLoading] = useState(false);

  const handleFileChange = (event) => {
    const selectedFiles = Array.from(event.target.files);
    setFiles(selectedFiles);
  };

  const handleUpload = async () => {
    if (files.length === 0) {
      alert("Seleccioná al menos una imagen.");
      return;
    }

    setLoading(true);
    const newTexts = {};

    for (const file of files) {
      const formData = new FormData();
      formData.append("file", file);

      try {
        const response = await fetch("http://backend:8000/ocr/", {
          method: "POST",
          body: formData,
        });

        const data = await response.json();
        newTexts[file.name] = data.text; // Guarda el texto extraído para cada imagen
      } catch (error) {
        console.error("Error:", error);
        newTexts[file.name] = "❌ Error al procesar la imagen";
      }
    }

    setTexts(newTexts);
    setLoading(false);
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gray-100 p-4">
      <h1 className="text-3xl font-bold mb-4">🔍 OCR - Subí una o varias imágenes</h1>

      <input
        type="file"
        accept="image/*"
        multiple
        onChange={handleFileChange}
        className="mb-4 border p-2"
      />

      <button
        onClick={handleUpload}
        className="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600"
        disabled={loading}
      >
        {loading ? "Procesando..." : "Extraer Texto"}
      </button>

      {/* Vista previa de imágenes */}
      <div className="mt-4 grid grid-cols-1 md:grid-cols-2 gap-4">
        {files.map((file) => (
          <div key={file.name} className="bg-white p-4 rounded shadow">
            <img src={URL.createObjectURL(file)} alt={file.name} className="w-full h-32 object-cover rounded mb-2" />
            <p className="text-sm text-gray-700 font-semibold">{file.name}</p>
            <p className="text-gray-700">{texts[file.name] || "⏳ Procesando..."}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
