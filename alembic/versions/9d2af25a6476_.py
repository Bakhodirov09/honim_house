"""empty message

Revision ID: 9d2af25a6476
Revises: 7c4f8a277c00
Create Date: 2024-03-20 21:41:23.331411

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9d2af25a6476'
down_revision: Union[str, None] = '7c4f8a277c00'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('logo')
    op.drop_table('filials')
    op.drop_table('ordering')
    op.drop_table('filial_admins')
    op.add_column('fast_food_menu', sa.Column('name', sa.String(), nullable=True))
    op.drop_column('fast_food_menu', 'food_name')
    op.drop_column('menu', 'menu_picture')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('menu', sa.Column('menu_picture', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('fast_food_menu', sa.Column('food_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('fast_food_menu', 'name')
    op.create_table('filial_admins',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('which_filial', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('admin_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('chat_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='filial_admins_pkey')
    )
    op.create_table('ordering',
    sa.Column('chat_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('status', sa.BOOLEAN(), autoincrement=False, nullable=True)
    )
    op.create_table('filials',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('filial_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('latitude', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('longitude', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('lang', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('is_open', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='filials_pkey')
    )
    op.create_table('logo',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('photo', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='logo_pkey')
    )
    # ### end Alembic commands ###