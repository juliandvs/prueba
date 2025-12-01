# app/api.py

from fastapi import FastAPI
from app.routers import contacto

app = FastAPI(title="HubSpot CRM Integración")

app.include_router(contacto.router)

@app.get("/")
async def root():
    return {"msg": "Servicio de Integración HubSpot en funcionamiento."}