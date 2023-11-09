"""create_user_table

Revision ID: 716055034d70
Revises: 
Create Date: 2023-11-09 10:27:27.106896

"""
import sqlalchemy as sa
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '716055034d70'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('username', sa.String, nullable=False),
        sa.Column('password', sa.String, nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
