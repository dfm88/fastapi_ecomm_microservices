"""empty message

Revision ID: b54376cae99b
Revises: e62435c6512f
Create Date: 2022-08-22 21:33:39.016560

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = 'b54376cae99b'
down_revision = 'e62435c6512f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('address', sa.Column('postal_code', sa.String(length=16), nullable=True))
    op.add_column('address', sa.Column('country', sa.String(length=256), nullable=True))
    op.drop_column('address', 'st_number')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('address', sa.Column('st_number', sa.VARCHAR(length=16), autoincrement=False, nullable=True))
    op.drop_column('address', 'country')
    op.drop_column('address', 'postal_code')
    # ### end Alembic commands ###