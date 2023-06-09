import requests
import logging
from database import create_api_call

HUBSPOT_ACCESS_TOKEN = "pat-na1-bfa3f0c0-426b-4f0e-b514-89b20832c96a"

async def create_contact_in_hubspot(contact_data, db):
    url = "https://api.hubapi.com/crm/v3/objects/contacts"

    headers = {
        "Authorization": f"Bearer {HUBSPOT_ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=contact_data, headers=headers)
    response.raise_for_status()

    contact_id = response.json().get("id")

    # Registrar la llamada a la API en la base de datos
    create_api_call(db, url, contact_data, response.text)

    logging.info("Contact created in HubSpot: %s", contact_id)

    return contact_id

async def get_hubspot_contacts():
    url = "https://api.hubapi.com/crm/v3/objects/contacts"
    headers = {
        "Authorization": f"Bearer {HUBSPOT_ACCESS_TOKEN}"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    contacts = response.json().get("results", [])
    return contacts
