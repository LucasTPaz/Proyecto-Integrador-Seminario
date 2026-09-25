# App mínima de Streamlit

Aplicación de ejemplo en Streamlit con un campo para escribir tu nombre y un botón de saludo.

## Requisitos

- Python 3.10 o superior
- Windows PowerShell

## Preparar el entorno

El entorno virtual de este proyecto se encuentra en `.venv`. Para crearlo e instalar las dependencias manualmente:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Si PowerShell bloquea la activación del entorno, puedes ejecutar Streamlit directamente:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

## Ejecutar la aplicación

Con el entorno activado:

```powershell
streamlit run app.py
```

Streamlit abrirá la aplicación en el navegador, normalmente en <http://localhost:8501>.