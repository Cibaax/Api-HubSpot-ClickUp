# API de Sincronización de Contactos

Esta es una API REST en Python que permite crear contactos en HubSpot y sincronizarlos con ClickUp, mientras registra cada llamada a la API en una base de datos PostgreSQL. 

## Requisitos

- Python 3.8 o superior
- Dependencias del proyecto (instaladas automáticamente durante el proceso de configuración)

## Configuración

1. Clona el repositorio o descarga los archivos del proyecto.
2. Asegúrate de tener instalada la versión correcta de Python.
3. Instala las dependencias ejecutando el siguiente comando:

   ```bash
   pip install -r requirements.txt
   ```

4. Asegúrate de tener acceso a la base de datos PostgreSQL con los siguientes detalles:

   - Host: db.g97.io
   - Puerto: 5432
   - Usuario: developer
   - Contraseña: qS*7Pjs3v0kw
   - Nombre de la base de datos: data_analyst

5. Verifica que tengas los tokens de acceso necesarios para HubSpot y ClickUp:

   - HubSpot Access Token: `pat-na1-bfa3f0c0-426b-4f0e-b514-89b20832c96a`
   - ClickUp API Token: `pk_3182376_Q233NZDZ8AVULEGGCHLKG2HFXWD6MJLC`
   - ClickUp List ID: `900200532843`

## Uso

1. Ejecuta el comando 
   ```
   uvicorn main:app --reload
   ```

### Endpoint: Crear contacto en HubSpot

- URL: `/contacts/hubspot`
- Método: `POST`
- Parámetros requeridos: `contact_data` (datos del contacto en formato JSON)

  Ejemplo de datos del contacto:
  ```json
  {
    "email": "test@orbidi.com",
    "firstname": "Test",
    "lastname": "Orbidi",
    "phone": "(322) 123-4567",
    "website": "orbidi.com"
  }
  ```

- Respuesta exitosa:

  ```json
  {
    "message": "Contact created in HubSpot",
    "contact_id": "<contact_id>"
  }
  ```

- Respuesta en caso de error: 
  - Código de estado: 500
  - Detalles: Descripción del error específico

### Endpoint: Sincronizar contactos entre HubSpot y ClickUp

- URL: `/contacts/sync`
- Método: `POST`

- Respuesta exitosa:

  ```json
  {
    "message": "Contact synchronization started"
  }
  ```

- Respuesta en caso de error: 
  - Código de estado: 500
  - Detalles: Descripción del error específico

## Registros de API

Todas las llamadas a los endpoints se registran en una base de datos PostgreSQL. Puedes encontrar los registros en la tabla `api_calls`, que contiene los siguientes campos:

- `id`: ID del registro
- `endpoint`: Endpoint llamado
- `params`: Parámetros enviados
- `result`: Resultado de la operación
- `created_at`: Fecha y hora de la llamada

## Recursos

- [HubSpot Contacts API](https://developers.hubspot.com/docs/api/crm/contacts)
- [ClickUp API](https://clickup.com/api/)

