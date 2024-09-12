"""Renaming students to scholars

Revision ID: ab3672ea4d11
Revises: 791279dd0760
Create Date: 2024-09-12 23:40:13.665961

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab3672ea4d11'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')
    


def downgrade() -> None:
    op.rename_table('scholars', 'students')
   
