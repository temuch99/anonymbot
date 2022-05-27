"""create user table

Revision ID: 48cf2d7f0783
Revises: 
Create Date: 2022-05-17 19:39:36.834585

"""
from datetime import datetime
from email.policy import default
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48cf2d7f0783'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(50), nullable=False)
    )


def downgrade():
    op.drop_table('user')
