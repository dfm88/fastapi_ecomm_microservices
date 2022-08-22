"""empty message

Revision ID: a9c22a3798e8
Revises: db8876aa09b9
Create Date: 2022-08-22 21:22:31.087392

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = 'a9c22a3798e8'
down_revision = 'db8876aa09b9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('address', sa.Column('street', sa.String(length=256), nullable=True))
    op.add_column('address', sa.Column('city', sa.String(length=256), nullable=True))
    op.add_column('address', sa.Column('st_number', sa.String(length=16), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('address', 'st_number')
    op.drop_column('address', 'city')
    op.drop_column('address', 'street')
    # ### end Alembic commands ###
