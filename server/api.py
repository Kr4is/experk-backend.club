from fastapi import FastAPI
from fastapi.responses import JSONResponse
from server.routes import router as HelloRouter
from server import crud

app = FastAPI()


@app.get("/", tags=["Root"])
async def read_root():
    return JSONResponse({"message": "Welcome to Hello World"}, status_code=200)

@app.get("/cities")
def get_cities():
    cities = crud.get_cities()
    print(f"cities: {cities}")
    return cities

@app.get("/experiences")
def get_experiences():
    experiences = crud.get_experiences()
    print(f"experiences: {experiences}")
    return experiences


app.include_router(HelloRouter)
