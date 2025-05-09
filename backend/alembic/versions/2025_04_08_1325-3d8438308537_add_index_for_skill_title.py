"""add index for skill title

Revision ID: 3d8438308537
Revises: c556649facab
Create Date: 2025-04-08 13:25:19.753908

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "3d8438308537"
down_revision: Union[str, None] = "c556649facab"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f("ix_skills_title"), "skills", ["title"], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_skills_title"), table_name="skills")
    # ### end Alembic commands ###
