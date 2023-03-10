"""add user table1

Revision ID: 573c77cb0ecd
Revises: 423538a649a3
Create Date: 2022-12-17 15:14:33.365816

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '573c77cb0ecd'
down_revision = '423538a649a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.Text(), nullable=False))
        batch_op.drop_column('passeword')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('passeword', sa.TEXT(), nullable=False))
        batch_op.drop_column('password')

    # ### end Alembic commands ###
