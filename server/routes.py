from fastapi import APIRouter
from fastapi.responses import JSONResponse
from server.model import HelloSchema
from typing import AnyStr

router = APIRouter()


@router.get("/hello", response_model=HelloSchema)
async def Hello_World() -> JSONResponse:
    return JSONResponse({"error": False, "message": "Hello World!"}, status_code=200)


@router.get("/hello/{name}", response_model=HelloSchema)
async def Hello_Name(name: AnyStr) -> JSONResponse:
    if not len(name):
        return JSONResponse(
            {"error": True, "message": "Please insert name in URL!"}, status_code=400
        )
    return JSONResponse({"error": False, "message": f"Hello {name}!"}, status_code=200)
