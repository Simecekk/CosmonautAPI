from fastapi import APIRouter, HTTPException

from astronauts.models import Astronaut
from astronauts.types import AstronautType, AstronautInputType
from core.settings import database

router = APIRouter()


@router.get(
    '/{pk}/',
    description='Astronaut detail endpoint',
)
async def get_astronaut(pk: int) -> AstronautType:
    query = Astronaut.select().where(Astronaut.c.id == pk)
    astronaut = await database.fetch_one(query)
    if not astronaut:
        raise HTTPException(status_code=404, detail="Object not found")
    return astronaut


@router.get(
    '/',
    description='Astronaut list endpoint',
)
async def get_astronauts(
    limit: int = 10,
    offset: int = 0,
) -> list[AstronautType]:
    query = Astronaut.select().limit(limit).offset(offset)
    return await database.fetch_all(query)


@router.post(
    '/',
    description='Astronaut create endpoint',
)
async def create_astronaut(astronaut: AstronautInputType) -> AstronautType:
    query = Astronaut.insert().values(**astronaut.model_dump())
    last_record_id = await database.execute(query)
    return AstronautType(id=last_record_id, **astronaut.model_dump())


@router.put(
    '/{pk}/',
    description='Astronaut update endpoint',
)
async def update_astronaut(pk: int, astronaut: AstronautInputType) -> AstronautType:
    query = Astronaut.update().where(Astronaut.c.id == pk).values(**astronaut.model_dump())
    await database.execute(query)
    return AstronautType(id=pk, **astronaut.model_dump())


@router.delete(
    '/{pk}/',
    description='Astronaut delete endpoint',
)
async def delete_astronaut(pk: int) -> bool:
    query = Astronaut.delete().where(Astronaut.c.id == pk)
    await database.execute(query)
    return True


@router.delete(
    "/delete/all/",
    description="Astronaut delete all endpoint",
)
async def delete_all_astronauts() -> bool:
    query = Astronaut.delete()
    await database.execute(query)
    return True
