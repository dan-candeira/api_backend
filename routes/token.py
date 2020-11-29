from fastapi import APIRouter
from models.user import Token, User

router = APIRouter()


@router.post('/', response_model=Token)
async def login_for_access_token():
    return
