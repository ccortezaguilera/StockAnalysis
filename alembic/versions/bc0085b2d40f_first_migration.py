"""First migration

Revision ID: bc0085b2d40f
Revises:
Create Date: 2020-11-08 20:33:03.254790

"""
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

from alembic import op

# revision identifiers, used by Alembic.
revision = "bc0085b2d40f"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "stock",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("modified_at", sa.DateTime(), nullable=False),
        sa.Column("ticker", sa.String(length=10), nullable=False),
        sa.PrimaryKeyConstraint("ticker"),
    )
    op.create_table(
        "stockday",
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("modified_at", sa.DateTime(), nullable=False),
        sa.Column(
            "id",
            sa.BigInteger()
            .with_variant(mysql.BIGINT(), "mysql")
            .with_variant(sa.BIGINT(), "postgresql")
            .with_variant(sa.INTEGER(), "sqlite"),
            nullable=False,
            autoincrement=True,
        ),
        sa.Column("close", sa.Float(), nullable=True),
        sa.Column("date", sa.DateTime(), nullable=True),
        sa.Column("high", sa.Float(), nullable=True),
        sa.Column("low", sa.Float(), nullable=True),
        sa.Column("open", sa.Float(), nullable=True),
        sa.Column(
            "volume",
            sa.BigInteger()
            .with_variant(mysql.BIGINT(), "mysql")
            .with_variant(sa.BIGINT(), "postgresql")
            .with_variant(sa.INTEGER(), "sqlite"),
            nullable=True,
        ),
        sa.Column("stock_id", sa.String(length=10), nullable=True),
        sa.ForeignKeyConstraint(
            ["stock_id"],
            ["stock.ticker"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("stockday")
    op.drop_table("stock")
    # ### end Alembic commands ###
