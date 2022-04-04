from sqladmin import ModelAdmin

from models import Todos


class TodoAdmin(ModelAdmin, model=Todos):
    column_list = [
        Todos.id,
        Todos.title,
        Todos.description,
        Todos.priority,
        Todos.complete,
        Todos.owner_id
    ]
