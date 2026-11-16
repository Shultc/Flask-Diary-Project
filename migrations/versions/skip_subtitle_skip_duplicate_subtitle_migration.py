"""skip duplicate subtitle migration

Revision ID: skip_subtitle
Revises: eaafea888508
Create Date: 2026-11-16 15:04:11.640149

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'skip_subtitle'
down_revision = 'eaafea888508'
branch_labels = None
depends_on = None


def upgrade():
    pass


def downgrade():
    pass
