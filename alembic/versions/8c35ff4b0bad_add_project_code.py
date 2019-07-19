"""Add project code

Revision ID: 8c35ff4b0bad
Revises: d0827785318a
Create Date: 2018-09-05 11:41:02.352902

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "8c35ff4b0bad"
down_revision = "d0827785318a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "project", sa.Column("project_code", sa.Unicode(length=45), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("project", "project_code")
    # ### end Alembic commands ###
