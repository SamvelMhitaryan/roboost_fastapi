"""add Questionnaire model

Revision ID: 87d6e5d9882d
Revises: aa67010732a0
Create Date: 2024-03-14 17:47:54.424280

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '87d6e5d9882d'
down_revision: Union[str, None] = 'aa67010732a0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questionnaires',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=70), nullable=False),
    sa.Column('surname', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('accounts', sa.String(), nullable=False),
    sa.Column('bithday_date', sa.Date(), nullable=False),
    sa.Column('alcohol', sa.Boolean(), nullable=False),
    sa.Column('smoking', sa.Boolean(), nullable=False),
    sa.Column('smoking_hqd', sa.Boolean(), nullable=False),
    sa.Column('current_employment', sa.Boolean(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('study', sa.Enum('YES', 'YES_BUT', 'NO', name='studyenum', native_enum=False, length=50), nullable=False),
    sa.Column('last_jobs', sa.String(length=500), nullable=False),
    sa.Column('achievements', sa.String(length=500), nullable=False),
    sa.Column('why_with_us', sa.String(length=500), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('phone')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('questionnaires')
    # ### end Alembic commands ###