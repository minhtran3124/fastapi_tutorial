import uvicorn
from fastapi import FastAPI

import models
from database import engine
from config import settings

from apis import router as api_router
from constants import API_V1


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(api_router, prefix=API_V1)


if __name__ == '__main__':
    uvicorn.run('__main__:app',
                host=settings.host,
                port=settings.port,
                reload=True,
                workers=2
            )
