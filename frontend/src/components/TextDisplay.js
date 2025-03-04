export default function TextDisplay({ extractedText }) {
  return (
    <div className="bg-accent w-full h-screen flex items-center justify-center p-8">
      <div className="bg-white text-black p-6 rounded-xl shadow-md w-full max-w-3xl border-4 border-highlight">
        <h2 className="text-2xl font-bold mb-4 text-center text-primary">Texto Extraído</h2>
        <p className="text-lg font-kanit text-gray-800 whitespace-pre-wrap">{extractedText || "Aún no hay texto..."}</p>
      </div>
    </div>
  );
}
