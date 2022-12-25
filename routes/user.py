from fastapi import APIRouter
from config.db import conn
from model.index import users
from schemas.index import User

user = APIRouter(prefix='/users')

@user.get('/')
async def read_data():
    return conn.execute(users.select()).fetchall()

@user.get('/{id}')
async def read_data_(id: int):
    return conn.execute(users.select().where(users.c.id == id)).fetchall()

@user.post('/')
async def write_data(user: User):
    conn.execute(users.insert().values(
        name=user.name,
        email=user.email,
        password=user.password
    ))
    return conn.execute(users.select()).fetchall()

@user.put('/{id}')
async def update_data(id: int, user: User):
    conn.execute(users.update(
        name=user.name,
        email=user.email,
        password=user.password
    ).where(users.c.id == id))
    return conn.execute(users.select()).fetchall()

@user.delete('/{id}')
async def delete_data(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    return conn.execute(users.select()).fetchall()
