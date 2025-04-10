"""delete is_active

Revision ID: b9182f951a9b
Revises: 3d8438308537
Create Date: 2025-04-09 00:59:06.558761

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b9182f951a9b"
down_revision: Union[str, None] = "3d8438308537"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "is_active")
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "users", sa.Column("is_active", sa.BOOLEAN(), nullable=False)
    )
    # ### end Alembic commands ###
