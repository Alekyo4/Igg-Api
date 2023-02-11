from fastapi import FastAPI
from uvicorn import run as uvicorn

from igg_api.router import app as router

app: FastAPI = FastAPI(title="Igg Api")

app.include_router(router)

def main() -> None:
    uvicorn("igg_api.main:app", host="0.0.0.0", reload=True)

if __name__ == "__main__":
    main()
