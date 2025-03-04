import '../app/globals.css'; // ✅ Importación sin alias para evitar errores

export default function App({ Component, pageProps }) {
  return <Component {...pageProps} />;
}
