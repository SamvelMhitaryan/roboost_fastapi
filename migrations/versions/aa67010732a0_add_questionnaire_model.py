"""add Questionnaire model

Revision ID: aa67010732a0
Revises: 019bc7dcc6c4
Create Date: 2024-03-14 17:18:57.991585

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aa67010732a0'
down_revision: Union[str, None] = '019bc7dcc6c4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('text', sa.String(length=500), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'text')
    # ### end Alembic commands ###
