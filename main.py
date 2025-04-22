import streamlit as st
from extractor import extraer_texto_pdf
from resumen import resumir_sentencia
import tempfile

st.set_page_config(page_title="Resumen Jurisprudencial Express", layout="centered")
st.title("📄 Resumen Jurisprudencial Express")
st.markdown("Subí una sentencia en PDF y generamos un resumen jurídico automático.")

archivo_pdf = st.file_uploader("📎 Cargar PDF", type="pdf")

if archivo_pdf:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(archivo_pdf.read())
        ruta_pdf = tmp_file.name

    with st.spinner("📚 Extrayendo texto del PDF..."):
        texto = extraer_texto_pdf(ruta_pdf)

    if texto:
        st.success("✅ Texto extraído con éxito.")
        if st.button("📑 Generar resumen"):
            with st.spinner("✍️ Generando resumen jurídico..."):
                resumen = resumir_sentencia(texto)
                st.markdown("### 🧾 Resumen Jurídico")
                st.write(resumen)
    else:
        st.error("❌ No se pudo extraer texto del PDF.")
