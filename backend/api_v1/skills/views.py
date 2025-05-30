from fastapi import (
    APIRouter,
    status,
    Depends,
)
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import (
    Skill,
    SkillBase,
    SkillUpdate,
)
from core.models import db_helper
from . import crud

router = APIRouter(tags=["Skills"])


@router.get("/", response_model=list[Skill])
async def get_skills(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_skills(session=session)


@router.post("/create/", response_model=Skill, status_code=status.HTTP_201_CREATED)
async def create_skill(
    skill_in: SkillBase,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_skill(session=session, skill_in=skill_in)


@router.get("/title/{title}/", response_model=Skill)
async def get_skill(
    title: str, session: AsyncSession = Depends(db_helper.scoped_session_dependency)
):
    return await crud.get_skill(session=session, title=title)


@router.patch("/edit/{title}/", response_model=Skill)
async def update_skill(
    skill_update: SkillUpdate,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_skill(
        session=session, title=skill_update.title, new_title=skill_update.new_title
    )


@router.delete("/delete/{title}/")
async def delete_skill(
    skill: SkillBase,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.delete_skill(session=session, title=skill.title)
