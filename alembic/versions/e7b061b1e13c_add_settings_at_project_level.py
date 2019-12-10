"""Add settings at project level

Revision ID: e7b061b1e13c
Revises: 7a1f06b526c6
Create Date: 2019-12-09 17:55:11.021931

"""
from alembic import op
import sqlalchemy as sa
from formshare.models.formshare import JsonEncodedDict


# revision identifiers, used by Alembic.
revision = "e7b061b1e13c"
down_revision = "7a1f06b526c6"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "prjsettings",
        sa.Column("project_id", sa.Unicode(length=64), nullable=False),
        sa.Column("settings_key", sa.Unicode(length=64), nullable=False),
        sa.Column("settings_value", JsonEncodedDict(), nullable=True),
        sa.ForeignKeyConstraint(
            ["project_id"],
            ["project.project_id"],
            name=op.f("fk_prjsettings_project_id_project"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint(
            "project_id", "settings_key", name=op.f("pk_prjsettings")
        ),
        mysql_charset="utf8",
        mysql_engine="InnoDB",
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("prjsettings")
    # ### end Alembic commands ###
