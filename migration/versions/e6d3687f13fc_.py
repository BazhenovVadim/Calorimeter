"""empty message

Revision ID: e6d3687f13fc
Revises: 
Create Date: 2023-12-18 15:55:06.263813

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e6d3687f13fc'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('products',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('product_name', sa.String(), nullable=False),
    sa.Column('proteins', sa.Float(), nullable=False),
    sa.Column('fats', sa.Float(), nullable=False),
    sa.Column('carbs', sa.Float(), nullable=False),
    sa.Column('calories', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('products')
    # ### end Alembic commands ###
