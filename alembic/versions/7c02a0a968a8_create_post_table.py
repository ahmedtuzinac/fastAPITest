"""create_post_table

Revision ID: 7c02a0a968a8
Revises: 716055034d70
Create Date: 2023-11-09 10:34:56.910317

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from datetime import datetime

# revision identifiers, used by Alembic.
revision: str = '7c02a0a968a8'
down_revision: Union[str, None] = '716055034d70'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('content', sa.String, nullable=False),
        sa.Column('created', sa.DateTime, default=datetime.utcnow),
        sa.Column('owner_id', sa.Integer, nullable=False)    
    )
    op.create_foreign_key(
        'post_users_fk',
        source_table='posts',
        referent_table='users',
        local_cols=['owner_id'],
        remote_cols=['id'],
        ondelete='CASCADE'
    )
    
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
