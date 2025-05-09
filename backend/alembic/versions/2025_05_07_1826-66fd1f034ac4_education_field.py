"""education field

Revision ID: 66fd1f034ac4
Revises: dfde74824af2
Create Date: 2025-05-07 18:26:02.047717

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "66fd1f034ac4"
down_revision: Union[str, None] = "dfde74824af2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "profiles", sa.Column("education", sa.Text(), nullable=False)
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("profiles", "education")
    # ### end Alembic commands ###
