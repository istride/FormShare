"""Add columns to accept a collaboration

Revision ID: f02babf9a725
Revises: 387b1c2f9052
Create Date: 2019-07-12 18:24:14.631646

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f02babf9a725"
down_revision = "387b1c2f9052"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "userproject",
        sa.Column(
            "project_accepted",
            sa.INTEGER(),
            server_default=sa.text("'1'"),
            nullable=True,
        ),
    )
    op.add_column(
        "userproject", sa.Column("project_accepted_date", sa.DateTime(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("userproject", "project_accepted_date")
    op.drop_column("userproject", "project_accepted")
    # ### end Alembic commands ###
