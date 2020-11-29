from fastapi import FastAPI
from starlette.responses import RedirectResponse

from routes.user import router as UserRouter

ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

app = FastAPI(
    title="Motion Sense"
)


@app.get('/')
def read_root():
    return RedirectResponse('/docs')


app.include_router(UserRouter, prefix='/users')
