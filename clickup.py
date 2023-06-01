import requests
import logging
from database import create_api_call

CLICKUP_API_TOKEN = "pk_3182376_Q233NZDZ8AVULEGGCHLKG2HFXWD6MJLC"
CLICKUP_LIST_ID = "900200532843"

def sync_contacts_to_clickup(contacts, db):
    url = f"https://api.clickup.com/api/v2/list/{CLICKUP_LIST_ID}/task"

    headers = {
        "Authorization": CLICKUP_API_TOKEN,
        "Content-Type": "application/json"
    }

    for contact in contacts:
        contact_id = contact.get("id")
        contact_name = f"{contact.get('firstname')} {contact.get('lastname')}"

        if contact.get("estado_clickup"):
            continue

        task_data = {
            "name": contact_name,
            "description": f"Contact ID: {contact_id}",
            "status": "open"
        }

        response = requests.post(url, json=task_data, headers=headers)
        response.raise_for_status()

        create_api_call(db, "/contacts/sync", contact, response.json())

        logging.info("Contact synced to ClickUp: %s", contact_id)
