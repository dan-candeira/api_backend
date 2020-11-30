from fastapi import FastAPI
from starlette.responses import RedirectResponse

from routes.user import router as UserRouter
from routes.token import router as TokenRouter

app = FastAPI(
    title="Motion Sense"
)


@app.get('/')
def read_root():
    return RedirectResponse('/docs')


app.include_router(UserRouter, prefix='/users')
app.include_router(TokenRouter, prefix='/token')
