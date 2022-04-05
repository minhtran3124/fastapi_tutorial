from fastapi import Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


# Custom error message for validation handler
async def validation_exception_handler(request: Request,
                                       exc: RequestValidationError):
    detail = []
    for error in exc.errors():
        detail.append({
            'field': error['loc'][1],
            'msg': error['msg']
        })

    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                        content=jsonable_encoder(detail))
