"""add upgupg

Revision ID: 194b1e4823be
Revises: 121a12d5571c
Create Date: 2023-02-05 22:10:42.942903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '194b1e4823be'
down_revision = '121a12d5571c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('match', schema=None) as batch_op:
        batch_op.alter_column('numero_match',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)

    with op.batch_alter_table('mes_grid', schema=None) as batch_op:
        batch_op.alter_column('resultat',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
        batch_op.alter_column('etat',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
        batch_op.alter_column('date_fin',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
        batch_op.alter_column('correct_resultat',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('mes_grid', schema=None) as batch_op:
        batch_op.alter_column('correct_resultat',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
        batch_op.alter_column('date_fin',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
        batch_op.alter_column('etat',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
        batch_op.alter_column('resultat',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)

    with op.batch_alter_table('match', schema=None) as batch_op:
        batch_op.alter_column('numero_match',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)

    # ### end Alembic commands ###
