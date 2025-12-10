from http import HTTPStatus
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_zero.database import get_session
from fastapi_zero.models import User
from fastapi_zero.security import (
    create_access_token,
    verify_password,
)

OAuth2Form = Annotated[OAuth2PasswordRequestForm, Depends()]
Session = Annotated[AsyncSession, Depends(get_session)]
router = APIRouter(prefix='/auth', tags=['auth'])


@router.post('/token')
async def login_for_acess_token(
    form_data: OAuth2Form,
    session: Session,
):
    user = await session.scalar(
        select(User).where((User.email == form_data.username))
    )

    exception = HTTPException(
        status_code=HTTPStatus.UNAUTHORIZED,
        detail='Incorrect email or password',
    )

    if not user:
        raise exception

    if not verify_password(form_data.password, user.password):
        raise exception

    access_token = create_access_token(data={'sub': user.email})

    return {'access_token': access_token, 'token_type': 'Bearer'}
