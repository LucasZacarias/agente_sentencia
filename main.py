# prueba_resumen.py
from extractor import extraer_texto_pdf
from resumen import resumir_sentencia

texto = extraer_texto_pdf("descargas_pdf/_ 1178589.pdf")
resumen = resumir_sentencia(texto)

print("📝 RESUMEN GENERADO:\n")
print(resumen)
