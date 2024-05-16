"""creating base tables.

Revision ID: e95c824e01aa
Revises:
Create Date: 2024-05-01 13:02:30.630252

"""

from collections.abc import Sequence


# revision identifiers, used by Alembic.
revision: str = "e95c824e01aa"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
