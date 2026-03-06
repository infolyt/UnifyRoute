"""add prompt_json and response_text

Revision ID: bdcc5219d5d3
Revises: 0a5746722fe4
Create Date: 2026-03-07 02:31:08.162795

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bdcc5219d5d3'
down_revision: Union[str, Sequence[str], None] = '0a5746722fe4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('request_logs', sa.Column('prompt_json', sa.Text(), nullable=True))
    op.add_column('request_logs', sa.Column('response_text', sa.Text(), nullable=True))


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('request_logs', 'response_text')
    op.drop_column('request_logs', 'prompt_json')
