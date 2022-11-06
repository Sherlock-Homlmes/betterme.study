# default
from pydantic import BaseModel, Field
import datetime, pytz
from dataclasses import dataclass
from uuid import uuid4, UUID

# local
from .base import dtbs
db = dtbs['todolist']
from apps.study_tools.models import TodoList

@dataclass
class TodoListDB:

    user_id: int

    # check if user excist
    def check(self):
        user_todolist = db.find_one({'user_id': self.user_id})

        if user_todolist:
            return user_todolist["todolist"]
        self.new()
        return []

    # create new user data
    def new(self):
        db.insert_one({'user_id': self.user_id, "todolist": []})

    # create new todo
    def create(self, data: TodoList):
        user_todolist = self.check()

        if len(user_todolist) >= 50:
            raise TooManyTodo
         
        id_list = [x["id"] for x in user_todolist]
        for i in range(1, 51):
            if i not in id_list:
                id = i
                break
        data.id = id

        todo = Todo(user_id=self.user_id, **data.__dict__).__dict__
        user_todolist.append(todo)
        db.update_one({'user_id': self.user_id}, {"$set": { 'todolist': user_todolist }})
        
        return todo

    # list all todo of user
    def list_todo(self):
        data = db.find_one({'user_id': self.user_id})
        if data:
            return data["todolist"]
        return []

    # update todo 
    def update(self, data: TodoList):
        user_todolist = self.check()

        todo = Todo(user_id=self.user_id, updated_at=vn_time(), **data.__dict__).__dict__

        for i in range(len(user_todolist)):
            if data.id == user_todolist[i]["id"]:
                user_todolist[i] = todo
                break

        db.update_one({'user_id': self.user_id}, {"$set": { 'todolist': user_todolist }})
        return todo

    # delete todo
    def delete(self, id: int):
        user_todolist = self.check()

        for i in range(len(user_todolist)):
            if user_todolist[i]["id"] == id:
                user_todolist.remove(user_todolist[i])
                break

        db.update_one({'user_id': self.user_id}, {"$set": { 'todolist': user_todolist }})
        return True


# class
def vn_time():
    utc_now = pytz.utc.localize(datetime.datetime.utcnow())
    pst_now = utc_now.astimezone(pytz.timezone("Asia/Ho_Chi_Minh"))
    today =  datetime.datetime(pst_now.year , pst_now.month , pst_now.day, pst_now.hour, pst_now.minute)
    
    return today

class Todo(BaseModel):
    id: int
    
    title: str
    description: str = Field(default='')
    status: str = Field(default='TO-DO')
    necessary: str = Field(default='NORMAL')
    difficult: int = Field(default=3, ge=1, le=5)

    created_at: datetime.datetime = Field(default=vn_time())
    updated_at: datetime.datetime = Field(default=vn_time())
    user_id: int


# exception
class TooManyTodo(Exception):
    """An Exception raised when user reach 50 todos"""