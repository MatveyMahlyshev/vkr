from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from sqlalchemy import String
from typing import TYPE_CHECKING
from .base import Base

if TYPE_CHECKING:
    from .candidate_profile_skill_association import CandidateProfileSkillAssociation
    from .vacancy_skill_association import VacancySkillAssociation
    from .skill_test import SkillTest
    from .vacancy_response_tests import VacancyResponseTest


class Skill(Base):
    title: Mapped[str] = mapped_column(
        String(25), nullable=False, unique=True, index=True
    )

    skill_profiles: Mapped[list["CandidateProfileSkillAssociation"]] = relationship(
        back_populates="skill",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    skill_vacancies: Mapped[list["VacancySkillAssociation"]] = relationship(
        back_populates="skill",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    tests: Mapped[list["SkillTest"]] = relationship(
        back_populates="skill",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )

    response_tests: Mapped[list["VacancyResponseTest"]] = relationship(
        back_populates="skill",
        cascade="all, delete-orphan",
        passive_deletes=True,
    )
