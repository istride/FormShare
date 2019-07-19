"""Add download error

Revision ID: d541781210ed
Revises: d2f438c8546e
Create Date: 2018-11-25 22:47:29.115469

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d541781210ed"
down_revision = "d2f438c8546e"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "mediafile",
        sa.Column(
            "file_dwnlderror",
            sa.INTEGER(),
            server_default=sa.text("'0'"),
            nullable=True,
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("mediafile", "file_dwnlderror")
    # ### end Alembic commands ###
