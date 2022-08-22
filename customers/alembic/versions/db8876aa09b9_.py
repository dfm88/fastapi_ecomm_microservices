"""empty message

Revision ID: db8876aa09b9
Revises: a5dbaa3ec743
Create Date: 2022-08-22 21:01:43.380805

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = 'db8876aa09b9'
down_revision = 'a5dbaa3ec743'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_address_id'), 'address', ['id'], unique=False)
    op.create_table('customer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_customer_email'), 'customer', ['email'], unique=True)
    op.create_index(op.f('ix_customer_full_name'), 'customer', ['full_name'], unique=False)
    op.create_index(op.f('ix_customer_id'), 'customer', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_customer_id'), table_name='customer')
    op.drop_index(op.f('ix_customer_full_name'), table_name='customer')
    op.drop_index(op.f('ix_customer_email'), table_name='customer')
    op.drop_table('customer')
    op.drop_index(op.f('ix_address_id'), table_name='address')
    op.drop_table('address')
    # ### end Alembic commands ###