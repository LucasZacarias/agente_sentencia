import streamlit as st
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

# Configuración del endpoint y modelo
ENDPOINT = "https://models.github.ai/inference"
MODEL = "openai/gpt-4.1"

# Token GitHub desde secrets
TOKEN = st.secrets["GITHUB_TOKEN"]

# Cliente de Azure AI Inference
client = ChatCompletionsClient(
    endpoint=ENDPOINT,
    credential=AzureKeyCredential(TOKEN),
)


def resumir_sentencia(texto):
    try:
        respuesta = OpenAI.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Eres un abogado especializado en derecho procesal civil. "
                        "Tu tarea es leer el texto de una sentencia judicial y generar un resumen breve, preciso y claro, resaltando los hechos relevantes, la pretensión, los fundamentos jurídicos y la parte resolutiva, las partes del proceso con sus respectivos abogados."
                    ),
                },
                {"role": "user", "content": texto},
            ],
            temperature=0.3,
            max_tokens=10000,
        )
        return respuesta.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Error al generar el resumen: {e}"
