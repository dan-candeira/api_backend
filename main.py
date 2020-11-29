from fastapi import FastAPI
from starlette.responses import RedirectResponse

from routes.user import router as UserRouter

app = FastAPI()


@app.get('/')
def read_root():
    return RedirectResponse('/docs')


app.include_router(UserRouter, prefix='/users')
