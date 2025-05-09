"""age field and rename model Profile

Revision ID: ddc9b44e5d89
Revises: 66fd1f034ac4
Create Date: 2025-05-07 18:49:43.953238

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "ddc9b44e5d89"
down_revision: Union[str, None] = "66fd1f034ac4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "candidateprofiles",
        sa.Column("surname", sa.String(length=50), nullable=False),
        sa.Column("name", sa.String(length=50), nullable=False),
        sa.Column("patronymic", sa.String(length=50), nullable=True),
        sa.Column("age", sa.Integer(), nullable=False),
        sa.Column("about_candidate", sa.Text(), nullable=True),
        sa.Column("education", sa.Text(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id"),
    )
    op.create_table(
        "candidate_profile_skill_association",
        sa.Column("candidate_profile_id", sa.Integer(), nullable=False),
        sa.Column("skill_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.ForeignKeyConstraint(
            ["candidate_profile_id"],
            ["candidateprofiles.id"],
        ),
        sa.ForeignKeyConstraint(
            ["skill_id"],
            ["skills.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "candidate_profile_id", "skill_id", name="idx_unique_order_product"
        ),
    )
    op.drop_table("profile_skill_association")
    op.drop_table("profiles")
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "profiles",
        sa.Column("surname", sa.VARCHAR(length=50), nullable=False),
        sa.Column("name", sa.VARCHAR(length=50), nullable=False),
        sa.Column("patronymic", sa.VARCHAR(length=50), nullable=True),
        sa.Column("about_candidate", sa.TEXT(), nullable=True),
        sa.Column("user_id", sa.INTEGER(), nullable=False),
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.Column("education", sa.TEXT(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("user_id"),
    )
    op.create_table(
        "profile_skill_association",
        sa.Column("profile_id", sa.INTEGER(), nullable=False),
        sa.Column("skill_id", sa.INTEGER(), nullable=False),
        sa.Column("id", sa.INTEGER(), nullable=False),
        sa.ForeignKeyConstraint(
            ["profile_id"],
            ["profiles.id"],
        ),
        sa.ForeignKeyConstraint(
            ["skill_id"],
            ["skills.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint(
            "profile_id", "skill_id", name="idx_unique_order_product"
        ),
    )
    op.drop_table("candidate_profile_skill_association")
    op.drop_table("candidateprofiles")
    # ### end Alembic commands ###
