import gradio as gr
from huggingface_hub import InferenceClient

# Inicializamos el cliente de inferencia de Hugging Face
# Usaremos un modelo especializado en español para análisis de sentimientos (RoBERTuito)
CLIENT_MODEL = "pysentimiento/robertuito-sentiment-analysis"
client = InferenceClient(model=CLIENT_MODEL)

def clasificar_resenia(texto):
    """
    Función que recibe el texto de la reseña, consulta al modelo de IA
    y devuelve el sentimiento clasificado (positivo, neutro, negativo) con su puntaje.
    """
    if not texto.strip():
        return "Por favor, ingresa un texto válido para analizar."

    try:
        # Realizamos la inferencia usando la API de Hugging Face
        resultado = client.text_classification(texto)

        # El resultado suele ser una lista de diccionarios con la etiqueta y la puntuación
        # Ejemplo: [{'label': 'POS', 'score': 0.95}, ...]
        respuesta_formateada = ""
        for item in resultado:
            etiqueta = item.get('label')
            puntaje = item.get('score')
            respuesta_formateada += f"**Etiqueta:** {etiqueta} | **Confianza:** {puntaje:.4f}\n"

        return respuesta_formateada

    except Exception as e:
        return f"Ocurrió un error al procesar la solicitud: {str(e)}"

# Construcción de la interfaz web con Gradio
demo = gr.Interface(
    fn=clasificar_resenia,
    inputs=gr.Textbox(
        lines=3,
        placeholder="Escribe una reseña aquí (ej: 'El servicio fue rapidísimo y la comida excelente, volvería sin dudas')..."
    ),
    outputs=gr.Markdown(),
    title="Clasificador de Reseñas de Comercios con IA",
    description="Herramienta basada en el modelo RoBERTuito para clasificar automáticamente comentarios de clientes en positivos, neutros o negativos.",
    flagging_mode="never"
)

if __name__ == "__main__":
    demo.launch()