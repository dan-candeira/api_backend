from fastapi import FastAPI
from starlette.responses import RedirectResponse

from routes.user import router as UserRouter
from routes.token import router as TokenRouter
from routes.patient import router as PatientRouter
from routes.equipment import router as EquipmentRouter
from routes.collect import router as CollectRouter

app = FastAPI(
    title="Motion Sense"
)


@app.get('/')
def read_root():
    return RedirectResponse('/docs')


app.include_router(UserRouter, prefix='/users')
app.include_router(TokenRouter, prefix='/token')
app.include_router(PatientRouter, prefix='/patients')
app.include_router(EquipmentRouter, prefix='/equipments')
app.include_router(CollectRouter, prefix='/collects')
