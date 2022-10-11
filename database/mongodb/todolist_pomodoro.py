from .base import dtbs

db = dtbs['todolist_pomodoro']

class TodolistPomodoro():

    # create & get user data
    def __init__(self, user_id) -> None:
        self.user_id = user_id
        self.data = self.get_or_create()

    def create(self):
        data = {
            'user_id': self.user_id,
            'todolist': {},
            'pomodoro': {
                'count': 0,
                'default': (25, 5),
                'history': []
            }
        }
        db.insert_one(data)
        del data['_id']

        return data

    def get(self):
        return db.find_one({'user_id': self.user_id})
        
    def get_or_create(self):
        data = self.get()
        if not data:
            data = self.create()

        return data

    # CRUD todolist
    def insert_todo(self, task):
        pass

    def update_todo(self, task):
        pass

    def delete_todo(self, task):
        pass

    # CRUD pomodoro
    def update_pomodoro(self, default: tuple):
        pass

    def insert_pomodoro(self):
        pass

    

from datetime import datetime
from typing import Union
example_data = {
    'user_id': 100,
    'todolist': {
        "1": {
            'time': datetime,
            'content': str,
            'status': Union('todo', 'doing', 'done')
        }
    },
    'pomodoro': {
        'count': 0,
        'default': (25, 5),
        'history': [
            {
                'time': datetime,
                'section_time': int
            }
        ]
    }
}