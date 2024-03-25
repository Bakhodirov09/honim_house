"""empty message

Revision ID: fc0f47974a0d
Revises: 8350367705bc
Create Date: 2024-03-22 17:27:35.919712

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fc0f47974a0d'
down_revision: Union[str, None] = '8350367705bc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('foods_menu', sa.Column('lang', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('foods_menu', 'lang')
    # ### end Alembic commands ###
