import uvicorn
from fastapi import FastAPI
from sqladmin import Admin

from fastapi_pagination import add_pagination

import models
from admins import TodoAdmin, UserAdmin

from database import engine
from config import settings

from apis import router as api_router
from constants import API_V1


app = FastAPI()
admin = Admin(app, engine)

models.Base.metadata.create_all(bind=engine)

app.include_router(api_router, prefix=API_V1)


admin.register_model(UserAdmin)
admin.register_model(TodoAdmin)

add_pagination(app)


if __name__ == '__main__':
    uvicorn.run('__main__:app',
                host=settings.host,
                port=settings.port,
                reload=True,
                workers=2
            )
