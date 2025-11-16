from fastapi import FastAPI
import uvicorn

from checking_code.apps import apps_router


app = FastAPI()

app.include_router(router=apps_router)


def start():
    uvicorn.run(app="checking_code.main:app", reload=True)
