from sqladmin import ModelAdmin

from models import Users


class UserAdmin(ModelAdmin, model=Users):
    column_list = [
        Users.id,
        Users.email,
        Users.first_name,
        Users.last_name,
        Users.is_active
    ]
