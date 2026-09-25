# App minima de Streamlit

Aplicacion de ejemplo en Streamlit con un campo para escribir tu nombre y un
boton de saludo.

## Requisitos

- Python 3.10 o superior
- Windows PowerShell

## Preparar el entorno

Desde esta carpeta, crea y activa un entorno virtual e instala las dependencias:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Ejecutar la aplicacion

```powershell
streamlit run app.py
```

Streamlit abrira la aplicacion en <http://localhost:8501>.