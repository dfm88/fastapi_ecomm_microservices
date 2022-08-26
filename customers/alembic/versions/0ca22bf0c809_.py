"""empty message

Revision ID: 0ca22bf0c809
Revises: 
Create Date: 2022-08-25 14:48:18.381424

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = '0ca22bf0c809'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
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
    op.create_table('address',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('street', sa.String(length=256), nullable=True),
    sa.Column('city', sa.String(length=256), nullable=True),
    sa.Column('postal_code', sa.String(length=16), nullable=True),
    sa.Column('country', sa.String(length=256), nullable=True),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_address_id'), 'address', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_address_id'), table_name='address')
    op.drop_table('address')
    op.drop_index(op.f('ix_customer_id'), table_name='customer')
    op.drop_index(op.f('ix_customer_full_name'), table_name='customer')
    op.drop_index(op.f('ix_customer_email'), table_name='customer')
    op.drop_table('customer')
    # ### end Alembic commands ###
