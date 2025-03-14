"""added a phone_number column

Revision ID: 95a59c0fd665
Revises: a6cb3d03c826
Create Date: 2025-03-14 08:32:54.527498

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '95a59c0fd665'
down_revision: Union[str, None] = 'a6cb3d03c826'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('users',sa.Column('phone_number',sa.String(length=15)))


def downgrade() -> None:
    op.drop_column('users','phone_number')
