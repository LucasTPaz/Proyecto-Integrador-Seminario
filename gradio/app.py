import gradio as gr


def saludar(nombre: str) -> str:
    nombre = nombre.strip()
    if not nombre:
        return "Escribe tu nombre para recibir un saludo."
    return f"¡Hola, {nombre}!"


app = gr.Interface(
    fn=saludar,
    inputs=gr.Textbox(label="¿Cómo te llamas?"),
    outputs=gr.Textbox(label="Saludo"),
    title="Mi primera app con Gradio",
)


if __name__ == "__main__":
    app.launch()