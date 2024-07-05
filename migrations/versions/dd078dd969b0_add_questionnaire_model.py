"""add Questionnaire model

Revision ID: dd078dd969b0
Revises: 87d6e5d9882d
Create Date: 2024-03-14 17:52:26.658974

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dd078dd969b0'
down_revision: Union[str, None] = '87d6e5d9882d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('questionnaires', 'accounts',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('questionnaires', 'address',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('questionnaires', 'study',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.alter_column('questionnaires', 'last_jobs',
               existing_type=sa.VARCHAR(length=500),
               nullable=True)
    op.alter_column('questionnaires', 'achievements',
               existing_type=sa.VARCHAR(length=500),
               nullable=True)
    op.alter_column('questionnaires', 'why_with_us',
               existing_type=sa.VARCHAR(length=500),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('questionnaires', 'why_with_us',
               existing_type=sa.VARCHAR(length=500),
               nullable=False)
    op.alter_column('questionnaires', 'achievements',
               existing_type=sa.VARCHAR(length=500),
               nullable=False)
    op.alter_column('questionnaires', 'last_jobs',
               existing_type=sa.VARCHAR(length=500),
               nullable=False)
    op.alter_column('questionnaires', 'study',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    op.alter_column('questionnaires', 'address',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('questionnaires', 'accounts',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###
