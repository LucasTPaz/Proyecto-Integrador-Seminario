# Clasificador de resenas de comercios

Aplicacion web en Python y Gradio que analiza el sentimiento de una resena en
espanol mediante la API de Hugging Face y el modelo
`pysentimiento/robertuito-sentiment-analysis`.

## Requisitos

- Python 3.10 o superior

## Instalacion y ejecucion

Desde esta carpeta, crea y activa un entorno virtual e instala las dependencias:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

Gradio mostrara en la terminal la URL local para abrir la aplicacion.
