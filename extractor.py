import pdfplumber


def extraer_texto_pdf(ruta_pdf):
    texto_completo = ""

    try:
        with pdfplumber.open(ruta_pdf) as pdf:
            for i, pagina in enumerate(pdf.pages, start=1):
                texto_pagina = pagina.extract_text()
                if texto_pagina:
                    texto_completo += f"\n\n--- Página {i} ---\n\n"
                    texto_completo += texto_pagina
    except Exception as e:
        print(f"❌ Error al extraer texto del PDF: {e}")
        return ""

    return texto_completo.strip()


from extractor import extraer_texto_pdf

texto = extraer_texto_pdf("descargas_pdf/_ 1178589.pdf")
print("TEXTO EXTRAIDO")
print(texto[:1000])  # Imprime los primeros 1000 caracteres del texto extraído
