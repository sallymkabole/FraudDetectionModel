"""empty message

Revision ID: 59df671f5438
Revises: 33222da0a283
Create Date: 2019-03-07 03:50:21.611116

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59df671f5438'
down_revision = '33222da0a283'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transactions', sa.Column('t_status', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('transactions', 't_status')
    # ### end Alembic commands ###