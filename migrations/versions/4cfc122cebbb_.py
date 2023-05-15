"""empty message

Revision ID: 4cfc122cebbb
Revises: b75ecc269f2f
Create Date: 2023-05-15 17:31:13.729861

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4cfc122cebbb'
down_revision = 'b75ecc269f2f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('supplier',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('company_name', sa.String(length=120), nullable=False),
    sa.Column('homepage', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('company_name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('supplier')
    # ### end Alembic commands ###
