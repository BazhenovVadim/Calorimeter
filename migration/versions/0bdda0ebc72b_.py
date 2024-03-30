"""empty message

Revision ID: 0bdda0ebc72b
Revises: fab93e2570ca
Create Date: 2024-03-08 12:13:26.740315

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0bdda0ebc72b'
down_revision: Union[str, None] = 'fab93e2570ca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.alter_column('products', 'id', new_column_name='product_id')


def downgrade():
    op.alter_column('products', 'product_id', new_column_name='id')