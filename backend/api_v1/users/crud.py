from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import CreateUserWithProfile
from core.models import User, Profile


async def create_user_with_profile(
    session: AsyncSession, user_profile: CreateUserWithProfile
) -> dict:
    user = User(
        email=user_profile.user.email,
        password_hash=user_profile.user.password.get_secret_value(),
        role=user_profile.user.role,
    )
    session.add(user)
    await session.flush()

    profile = Profile(
        surname=user_profile.profile.surname,
        name=user_profile.profile.name,
        patronymic=user_profile.profile.patronymic,
        about_candidate=user_profile.profile.about_candidate,
        user_id=user.id,
    )
    session.add(profile)

    await session.commit()

    return {
        "user": user,
        "profile": profile,
    }
