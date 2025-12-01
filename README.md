Para el CRM



1. Iniciar hubspot con el siguiente correo pivote :
    correo : julianspam01407@gmail.com
    contra : juliandaviD14*_





Para fastAPI:

1. Clonar el repositorio
2. Crear el archivo (.env) en la raiz del proyecto y pegar lo siguiente : HUBSPOT_TOKEN={token_hubspot}
3. En la terminal, estando en la carpeta del proyecto ejecutar “python3 -m venv .venv” o “python -m venv .venv”
4. Activar el entorno virtual con “source .venv/bin/activate”
5. Actualizar pip con “python -m pip install --upgrade pip”
6. Instalar los requerimientos con “pip install -r requerimientos.txt”
7. Correr el servidor con “uvicorn app.api:app --reload”
8. Instalar ngrok dependiendo de su sistema operativo
9. Escribir en la terminal “ngrok config add-authtoken {token_ngrok}
10. Ejecutar “ngrok http 8000” que es donde se ejecuta el servidor de uvicorn
11. Para la url que se utilizara en n8n, se tomara del output de ngrok luego de utilizar el comando previo, en la parte que dice "Forwarding" se tomara la url.
12. Dependiendo de endpoint que queramos, primero se pone la url generada por ngrok y luego la ruta (/crm/contact​, /crm/contact/note​, /crm/contact/update)

Para n8n:

1. Se descarga el "Agente - Verticcal.json"
2. Importar el .json a n8n en la web
3. Ir al "Google Gemini Chat Model" y poner la {API KEY} de gemini 
4. (TENER CUIDADO) revisar si la url que esta ya establecida en los http tools es la misma que arroja ngrok y verificar si tienen el endpoint correspondiente, de lo contrario, se configuran los http requests tool con la url de ngrok y la ruta para cada tool Crear Usuario = /crm/contact​, Dejar Nota = /crm/contact/note​ Y Actualizar contacto = /crm/contact/update


Por ultimo se hacen las pruebas.
