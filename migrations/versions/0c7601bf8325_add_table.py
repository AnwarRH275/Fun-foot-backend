"""add table

Revision ID: 0c7601bf8325
Revises: 573c77cb0ecd
Create Date: 2023-02-01 22:36:23.432719

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c7601bf8325'
down_revision = '573c77cb0ecd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('numero_match', sa.String(length=100), nullable=False),
    sa.Column('categorie_match', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=False),
    sa.Column('date', sa.String(length=100), nullable=False),
    sa.Column('heure', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('category')
    # ### end Alembic commands ###
