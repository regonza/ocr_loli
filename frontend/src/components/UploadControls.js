
import { useState } from "react";

export default function UploadControls({ onUpload }) {
  const [files, setFiles] = useState([]);

  const handleFileChange = (e) => {
    if (e.target.files) {
      setFiles(Array.from(e.target.files));
    }
  };

  return (
    <div className="bg-primary p-6 rounded-xl shadow-lg text-black w-full max-w-md">
      <h2 className="text-2xl font-semibold mb-4">Carga de Imágenes</h2>
      <div className="flex flex-col gap-4">
        <input
          type="file"
          multiple
          accept="image/*"
          className="file:bg-secondary file:text-black file:font-bold file:border-none file:px-4 file:py-2 file:rounded-lg file:cursor-pointer w-full"
          onChange={handleFileChange}
        />
        <button
          onClick={() => onUpload(files)}
          className="mt-2 bg-highlight text-black font-semibold py-2 px-4 rounded-xl transition hover:bg-yellow-400"
        >
          Subir y Extraer Texto
        </button>
      </div>
    </div>
  );
}
