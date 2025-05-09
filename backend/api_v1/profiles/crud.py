from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends, HTTPException, status

from core.models import CandidateProfileSkillAssociation
from .schemas import CandidateProfileUser, CandidateProfileUpdate
from api_v1.skills.schemas import SkillBase
from api_v1.skills.crud import get_skill
from api_v1.dependencies import get_user, get_statement_for_candidate_profile
from core.models.user import UserRole


async def get_user_with_profile_by_token(
    session: AsyncSession, payload: dict
) -> CandidateProfileUser:

    user = await get_user(
        session=session,
        payload=payload,
        stmt=await get_statement_for_candidate_profile(payload=payload),
        user_role=UserRole.CANDIDATE,
    )

    if not user.candidate_profile:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Profile not found for this user",
        )

    return {
        "email": user.email,
        "role": user.role.value,
        "name": user.candidate_profile.name,
        "surname": user.candidate_profile.surname,
        "patronymic": user.candidate_profile.patronymic,
        "age": user.candidate_profile.age,
        "about_candidate": user.candidate_profile.about_candidate,
        "education": user.candidate_profile.education,
        "skills": [
            {"title": assoc.skill.title, "id": assoc.skill.id}
            for assoc in user.candidate_profile.profile_skills
        ],
    }


async def update_candidate_profile(
    profile_data: CandidateProfileUpdate, session: AsyncSession, payload: dict
):
    user_profile = await get_user(
        session=session,
        payload=payload,
        stmt=await get_statement_for_candidate_profile(payload=payload),
        user_role=UserRole.CANDIDATE,
    )
    user_profile.email = profile_data.email
    user_profile.name = profile_data.name
    user_profile.candidate_profile.surname = profile_data.surname
    user_profile.candidate_profile.patronymic = profile_data.patronymic
    user_profile.candidate_profile.age = profile_data.age
    user_profile.candidate_profile.about_candidate = profile_data.about_candidate
    user_profile.candidate_profile.education = profile_data.education

    await session.commit()

    return {
        "email": user_profile.email,
        "role": user_profile.role.value,
        "name": user_profile.candidate_profile.name,
        "surname": user_profile.candidate_profile.surname,
        "patronymic": user_profile.candidate_profile.patronymic,
        "age": user_profile.candidate_profile.age,
        "about_candidate": user_profile.candidate_profile.about_candidate,
        "education": user_profile.candidate_profile.education,
        "skills": [
            {"title": assoc.skill.title, "id": assoc.skill.id}
            for assoc in user_profile.candidate_profile.profile_skills
        ],
    }


async def update_candidate_profile_skills(
    skills: list[SkillBase], session: AsyncSession, payload: dict
) -> list[SkillBase]:
    user = await get_user(
        session=session,
        payload=payload,
        stmt=await get_statement_for_candidate_profile(payload=payload),
        user_role=UserRole.CANDIDATE,
    )

    for association in user.candidate_profile.profile_skills:
        await session.delete(association)

    await session.flush()

    for skill in skills:
        current_skill = await get_skill(session=session, title=skill.title)
        association = CandidateProfileSkillAssociation(
            candidate_profile_id=user.id, skill_id=current_skill.id
        )
        session.add(association)
    await session.commit()
    return skills
