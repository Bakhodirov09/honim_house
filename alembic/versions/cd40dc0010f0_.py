"""empty message

Revision ID: cd40dc0010f0
Revises: a3596cbd1d37
Create Date: 2024-03-23 23:32:48.131754

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cd40dc0010f0'
down_revision: Union[str, None] = 'a3596cbd1d37'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('curers', sa.Column('is_working', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('curers', 'is_working')
    # ### end Alembic commands ###
