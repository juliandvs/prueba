from dotenv import load_dotenv
import os

load_dotenv()

HUBSPOT_TOKEN = os.getenv('HUBSPOT_TOKEN')


HUBSPOT_MAPPING = {
    "nombre": "firstname",
    "telefono": "phone",
    "estado": "hs_lead_status"
}

def get_hubspot_headers():
    return{
        "Authorization": f"Bearer {HUBSPOT_TOKEN}",
        "Content-Type": "application/json"
    }