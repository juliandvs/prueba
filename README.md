Para el CRM



1. Iniciar hubspot con el siguiente correo pivote :
    correo : julianspam0714@gmail.com
    contra : juliandaviD14*_





Para fastAPI:

1. clonar el repositorio
2. crear el archivo (.env) en la raiz del proyecto y pegar lo siguiente : HUBSPOT_TOKEN={token_hubspot}
3. en la terminal, estando en la carpeta del proyecto ejecutar “python3 -m venv .venv” o “python -m venv .venv”
4. activar el entorno virtual con “source .venv/bin/activate”
5. actualizar pip con “python -m pip install --upgrade pip”
6. instalar los requerimientos con “pip install -r requerimientos.txt”
7. correr el servidor con “uvicorn app.api:app --reload”
8. instalar ngrok dependiendo de su sistema operativo
9. escribir en la terminal “ngrok config add-authtoken {token_ngrok}
10. ejecutar “ngrok http 8000” que es donde se ejecuta el servidor de uvicorn
11. para la url que se utilizara en n8n, se tomara del output de ngrok luego de utilizar el comando previo, en la parte que dice "Forwarding" se tomara la url.
12. dependiendo de endpoint que queramos, primero se pone la url generada por ngrok y luego la ruta (/crm/contact​, /crm/contact/note​, /crm/contact/update)

Para n8n:

1. se descarga el Agente - Verticcal.json
2. importar el .json a n8n en la web
3. se configuran los http requests tool con la url de ngrok y la ruta para cada tool Crear Usuario = /crm/contact​, Dejar Nota = /crm/contact/note​ Y Actualizar contacto = /crm/contact/update


Por ultimo se hacen las pruebas.
