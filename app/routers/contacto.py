# app/routers/contacto.py

from fastapi import APIRouter, HTTPException
from app.models.contact_models import Usuario, actualizar_usuario, dejar_nota
from app.config import HUBSPOT_MAPPING, get_hubspot_headers
import httpx
import re # Necesario para el manejo de errores de estado

router = APIRouter(tags=["Contactos CRM"])
HUBSPOT_BASE_URL = "https://api.hubapi.com/crm/v3/objects/contacts"


# === Endpoint para crear un contacto (POST) ===
@router.post("/crm/contact")
async def crear_contacto(contact: Usuario):
    hubspot_payload = {
        "properties":{
            "firstname": contact.nombre,
            "email": contact.correo,
            "phone": contact.telefono
        }
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                HUBSPOT_BASE_URL,
                json=hubspot_payload,
                headers=get_hubspot_headers()
            )
            response.raise_for_status()
            return {"message": "Contacto creado exitosamente en Hubspot."}
    except httpx.HTTPStatusError as e:
        error_details = e.response.json().get("message", "Error desconocido de HubSpot")
        raise HTTPException(status_code=500, detail=f"Error al crear contacto: {error_details}")


@router.patch("/crm/contact/note")
async def enviar_nota(nota: dejar_nota):

    hubspot_payload = {"properties": {'note': nota.nota}}
    correo = nota.correo
    hubspot_url = f"{HUBSPOT_BASE_URL}/{correo}?idProperty=email"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.patch(hubspot_url, json=hubspot_payload, headers=get_hubspot_headers())
            response.raise_for_status()
            return {"message": f"Nota actualizada con éxito para el correo {correo}."}
    
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            return {"success": False, "message": f"Lo siento, no se encontró ningún contacto con el correo {nota.correo} para actualizar.", "status": 404}
        error_details = e.response.json().get("message", "Error desconocido de HubSpot")
        raise HTTPException(status_code=500, detail=f"Error de actualizacion en Hubspot: {error_details}")


# === Endpoint para actualizar campos (PATCH /update) ===
@router.patch("/crm/contact/update")
async def actualizar_contacto(datos_usuario: actualizar_usuario):

    properties_to_update = {}

    for campo, valor in datos_usuario.model_dump(exclude_none=True).items():
        if campo == "correo":
            continue

        if campo == "estado":
            hubspot_name = HUBSPOT_MAPPING.get(campo)
            valor_mayusculas = str(valor).strip().upper() 

            if hubspot_name:
                properties_to_update[hubspot_name] = valor_mayusculas
            continue

        hubspot_name = HUBSPOT_MAPPING.get(campo)
        if hubspot_name:
            properties_to_update[hubspot_name] = valor
    
    if not properties_to_update:
        raise HTTPException(status_code=400, detail="Se requiere al menos un campo (nombre, telefono, nota o estado) para actualizar")

    hubspot_payload = {"properties": properties_to_update}
    correo_actualizar = datos_usuario.correo
    hubspot_url = f"{HUBSPOT_BASE_URL}/{correo_actualizar}?idProperty=email"

    try:
        async with httpx.AsyncClient() as client:
            response = await client.patch(hubspot_url, json=hubspot_payload, headers=get_hubspot_headers())
            response.raise_for_status()
            return {"sucess": True, "message": f"Campos actualizados con éxito para el correo {correo_actualizar}."}

    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            return {"sucess": False, "message": f"Lo siento, no se encontró ningún contacto con el correo {correo_actualizar} para actualizar."}

        # Manejo de error de estado inválido
        if e.response.status_code in [500, 400]: 
            try:
                error_json = e.response.json()
                validation_results = error_json.get("validationResults", [{}])
                
                if validation_results and "INVALID_OPTION" in validation_results[0].get("error", ""):
                    hubspot_message = validation_results[0].get("message", "")
                    match = re.search(r"\[(.+)\]", hubspot_message)
                    if match:
                        allowed_options = match.group(1).replace(",", ", ") 
                        return {"success": False, "message": f"El estado proporcionado no es válido. Los estados permitidos son: {allowed_options}.", "status": 400}
            except Exception:
                pass

        error_details = e.response.json().get("message", "Error desconocido de Hubspot")
        raise HTTPException(status_code=500, detail=f"Error de actualización: {error_details}")