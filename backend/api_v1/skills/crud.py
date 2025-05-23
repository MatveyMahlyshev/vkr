from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result
from fastapi import HTTPException, status

from .schemas import SkillBase
from core.models import Skill
import exceptions


def to_capitalize(string: str) -> str:
    return string.lower().capitalize()


async def get_skills(session: AsyncSession) -> list[Skill]:
    stmt = select(Skill).order_by(Skill.id)
    result: Result = await session.execute(statement=stmt)
    skills = list(result.scalars().all())
    return skills


async def get_skill(session: AsyncSession, title: str) -> Skill:
    title = to_capitalize(title)
    stmt = select(Skill).where(Skill.title == title)
    skill: Skill | None = await session.scalar(statement=stmt)
    if skill is None:
        raise exceptions.NotFoundException.SKILL_NOT_FOUND
    return skill

async def get_skill_by_id(session: AsyncSession, skill_id: int) -> Skill:
    stmt = select(Skill).where(Skill.id == skill_id)
    skill: Skill | None = await session.scalar(statement=stmt)
    if skill is None:
        raise exceptions.NotFoundException.SKILL_NOT_FOUND
    return skill


async def update_skill(
    session: AsyncSession, title: str, new_title: str
) -> Skill | None:
    new_title = to_capitalize(new_title)
    stmt = select(Skill).where(Skill.title == new_title)
    updated_skill: Skill | None = await session.scalar(statement=stmt)
    if updated_skill is not None:
        raise exceptions.ConflictException.SKILL_ALREADY_EXISTS
    skill = await get_skill(session=session, title=title)
    new_title = to_capitalize(new_title)
    skill.title = new_title
    await session.commit()
    return skill


async def create_skill(session: AsyncSession, skill_in: SkillBase) -> Skill:
    stmt = select(Skill).where(Skill.title == skill_in.title)
    exists: Skill | None = await session.scalar(statement=stmt)
    if exists:
        raise exceptions.ConflictException.SKILL_ALREADY_EXISTS
    skill = Skill(**skill_in.model_dump())
    skill.title = to_capitalize(skill.title)
    session.add(skill)
    await session.commit()

    return skill


async def delete_skill(session: AsyncSession, title: str) -> None:
    skill = await get_skill(
        session=session,
        title=title,
    )

    await session.delete(skill)
    await session.commit()

    return None
