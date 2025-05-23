from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from .schemas import CreateUserWithProfile, UserCreate
from . import crud

router = APIRouter(tags=["Users"])


@router.post("/register/candidate/", status_code=status.HTTP_201_CREATED)
async def create_user_with_profile(
    user_profile: CreateUserWithProfile,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_user_with_profile(
        session=session, user_profile=user_profile
    )


@router.post("/register/hr/", status_code=status.HTTP_201_CREATED)
async def create_user(
    user: UserCreate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_user(session=session, user=user)
