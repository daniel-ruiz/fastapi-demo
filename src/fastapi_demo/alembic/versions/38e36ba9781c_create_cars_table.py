"""Create cars table

Revision ID: 38e36ba9781c
Revises:
Create Date: 2020-12-10 01:20:50.752545

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38e36ba9781c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'cars',
        sa.Column('id', sa.INTEGER(), nullable=False),
        sa.Column('make', sa.VARCHAR(), nullable=True),
        sa.Column('model', sa.VARCHAR(), nullable=True),
        sa.Column('year', sa.INTEGER(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('cars')
