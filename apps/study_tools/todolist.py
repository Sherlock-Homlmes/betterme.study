# default
from typing import List

# fastapi
from fastapi import Depends
from fastapi.responses import JSONResponse

#auth
from apps.authentication import discord, User

#local
from . import router
from base.settings import app
from .models import TodoList
from database.mongodb import TodoListDB, TooManyTodo, Todo


@router.get(
    '/todolist',
    dependencies=[Depends(discord.requires_authorization)],
    response_model= List[Todo]
)
async def todolist(user: User = Depends(discord.user)):
    todo_list = TodoListDB(user.id).list_todo()
    return todo_list


@router.post(
    '/todolist',
    dependencies=[Depends(discord.requires_authorization)],
    response_model= Todo
)
async def todolist(user: User = Depends(discord.user), todo = Depends(TodoList)):
    todo = TodoListDB(user.id).create(todo)
    return todo


@router.put(
    '/todolist',
    dependencies=[Depends(discord.requires_authorization)],
    response_model= Todo
)
async def todolist(user: User = Depends(discord.user), todo = Depends(TodoList)):
    todo = TodoListDB(user.id).update(todo)
    return todo


@router.delete(
    '/todolist',
    dependencies=[Depends(discord.requires_authorization)]
)
async def todolist(id: int, user: User = Depends(discord.user)):
    TodoListDB(user.id).delete(id)
    return JSONResponse({"message": f"success delete todo id {id}"}, status_code=200)

# exception
@app.exception_handler(TooManyTodo)
async def client_session_error_handler(_, e: TooManyTodo):
    print(e)
    return JSONResponse({"error": "Internal Error"}, status_code=500)