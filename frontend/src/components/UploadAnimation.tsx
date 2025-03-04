import React, { useState } from "react";
import { motion } from "framer-motion"

export default function UploadAnimation({ onFilesSelected }) {
  const [uploaded, setUploaded] = useState(false);

  const handleFileChange = (event) => {
    const selectedFiles = Array.from(event.target.files);
    if (selectedFiles.length > 0) {
      setUploaded(true);
      onFilesSelected(selectedFiles); // Enviamos los archivos al componente padre
    }
  };

  return (
    <div className="flex flex-col items-center justify-center">
      <motion.div
        initial={{ opacity: 0, scale: 0.8 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.5, ease: "easeOut" }}
        className="bg-white p-6 rounded-2xl shadow-xl"
      >
        {!uploaded ? (
          <motion.label
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            className="cursor-pointer flex flex-col items-center"
          >
            <input
              type="file"
              accept="image/*"
              multiple
              className="hidden"
              onChange={handleFileChange}
            />
            <motion.div
              initial={{ y: -10, opacity: 0 }}
              animate={{ y: 0, opacity: 1 }}
              transition={{ duration: 0.4, ease: "easeOut" }}
              className="w-20 h-20 bg-blue-500 rounded-full flex items-center justify-center text-white text-3xl"
            >
              📤
            </motion.div>
            <p className="mt-2 text-gray-600">Sube tus imágenes</p>
          </motion.label>
        ) : (
          <motion.div
            initial={{ y: 10, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            transition={{ duration: 0.5, ease: "easeOut" }}
            className="text-green-500 text-lg font-semibold"
          >
            ¡Imágenes seleccionadas!
          </motion.div>
        )}
      </motion.div>
    </div>
  );
}
