from fastapi import FastAPI, BackgroundTasks, Depends
from database import get_db, create_api_call, setup_database
from hubspot import create_contact_in_hubspot, get_hubspot_contacts
from clickup import sync_contacts_to_clickup
from fastapi import HTTPException
import logging


app = FastAPI()

@app.on_event("startup")
async def startup_event():
    setup_database()
    logging.basicConfig(filename='api.log', level=logging.INFO)



@app.post("/contacts/hubspot")
async def create_hubspot_contact(contact_data: dict, background_tasks: BackgroundTasks, db=Depends(get_db)):
    try:
        contact_id = await create_contact_in_hubspot(contact_data, db)
        background_tasks.add_task(create_api_call, db, "/contacts/hubspot", contact_data, contact_id)
        return {"message": "Contact created in HubSpot", "contact_id": contact_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/contacts/sync")
async def sync_contacts(background_tasks: BackgroundTasks, db=Depends(get_db)):
    contacts = await get_hubspot_contacts()
    background_tasks.add_task(sync_contacts_to_clickup, contacts, db)
    return {"message": "Contact synchronization started"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
