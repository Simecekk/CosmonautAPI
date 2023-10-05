from fastapi import FastAPI, status

from astronauts.endpoints import router as astronauts_router
from astronauts.import_consumer import AstronautImportConsumer
from core import settings
from core.settings import database

app = FastAPI(title="International Space Station API", version='1.0', debug=settings.DEBUG)

app.include_router(
    astronauts_router,
    prefix="/api/v1/astronauts",
    responses={status.HTTP_404_NOT_FOUND: {"description": "Not found"}},
)


@app.on_event("startup")
async def start_event():
    await database.connect()
    astronaut_consumer = AstronautImportConsumer()
    await astronaut_consumer.start_consumer()


@app.on_event("shutdown")
async def shutdown_event():
    await database.disconnect()


@app.get(
    "/",
    description="Check if the API is alive",
)
async def is_alive() -> bool:
    return True
