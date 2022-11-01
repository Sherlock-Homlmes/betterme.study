# fastapi
from fastapi import Request, Depends
from fastapi.responses import JSONResponse
from pydantic.error_wrappers import ValidationError

#auth
from apps.authentication import discord, User

#local
from . import router
from base import TemplateResponse
from .models import TodoList
from database.mongodb import TodoListDB

@router.api_route(
    '/todolist', 
    methods=['GET','PUT','PATCH','DELETE'],
    dependencies=[Depends(discord.requires_authorization)],
    response_model=None
)
async def todolist(request: Request, user: User = Depends(discord.user)):
    
    if request.method == 'GET':
        return TodoListDB().list_todo(user.id)

    elif request.method == 'PUT':
        data = await request.json()
        print(data)
        try: 
            todo = TodoList(
                user_id=user.id, 
                title=data["title"],
                description=data["description"],
                status=data["status"],
                necessary=data["necessary"],
                difficult=data["difficult"],
            )
        except KeyError as e:
            return JSONResponse({"error": "Key error", "detail": str(e)}, status_code=400)
        except ValidationError as e:
            return JSONResponse({"error": "Validate error", "detail": str(e)}, status_code=400)

        user_todo = TodoListDB().create(todo)

        return "oke"

    elif request.method == 'PATCH':
        pass

    elif request.method == 'DELETE':
        pass
