"""Add sample cars

Revision ID: ea66c3f9efd5
Revises: 38e36ba9781c
Create Date: 2020-12-11 23:54:26.868840

"""
from alembic import op
from sqlalchemy import Integer, String
from sqlalchemy.sql import table, column


# revision identifiers, used by Alembic.
revision = 'ea66c3f9efd5'
down_revision = '38e36ba9781c'
branch_labels = None
depends_on = None


def upgrade():
    cars = table(
        'cars',
        column('id', Integer),
        column('make', String),
        column('model', String),
        column('year', Integer),
    )

    sample_cars = [
        {'id': 1, 'make': 'Audi', 'model': 'A3', 'year':2005},
        {'id': 2, 'make': 'Mercedes-Benz', 'model': 'E', 'year':2003},
        {'id': 3, 'make': 'Tesla', 'model': 'Model S', 'year':2012},
    ]

    op.bulk_insert(cars, sample_cars)


def downgrade():
    pass
