"use client";
import { useState } from "react";
import UploadControls from "../components/UploadControls";
import TextDisplay from "../components/TextDisplay";

export default function Home() {
  const [extractedText, setExtractedText] = useState("");

  const handleUpload = async (files) => {
    if (files.length === 0) return alert("Selecciona al menos una imagen.");

    const API_URL =
      typeof window !== "undefined"
        ? "http://localhost:8000/ocr/"
        : "http://backend:8000/ocr/";

    const formData = new FormData();
    formData.append("file", files[0]); // Solo subimos una imagen por simplicidad

    const response = await fetch(API_URL, {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    setExtractedText(data.text || "No se pudo extraer texto.");
  };

  return (
    <main className="flex flex-col items-center justify-center gap-8 p-8 min-h-screen bg-gray-100">
      <UploadControls onUpload={handleUpload} />
      <TextDisplay extractedText={extractedText} />
    </main>
  );
}