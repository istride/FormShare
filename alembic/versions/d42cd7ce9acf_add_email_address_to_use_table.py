"""Add email address to use table

Revision ID: d42cd7ce9acf
Revises: d9a26c485a70
Create Date: 2018-08-21 11:01:28.085765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "d42cd7ce9acf"
down_revision = "d9a26c485a70"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        "fk_collaborator_samas_project_collaborator", "collaborator", type_="foreignkey"
    )
    op.create_foreign_key(
        op.f("fk_collaborator_samas_project_collaborator"),
        "collaborator",
        "collaborator",
        ["samas_project", "sameas_coll"],
        ["project_id", "coll_id"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        "fk_collingroup_project_id_collgroup", "collingroup", type_="foreignkey"
    )
    op.create_foreign_key(
        op.f("fk_collingroup_project_id_collgroup"),
        "collingroup",
        "collgroup",
        ["project_id", "group_id"],
        ["project_id", "group_id"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        "fk_formaccess_project_id_collaborator", "formaccess", type_="foreignkey"
    )
    op.create_foreign_key(
        op.f("fk_formaccess_project_id_collaborator"),
        "formaccess",
        "collaborator",
        ["project_id", "coll_id"],
        ["project_id", "coll_id"],
        ondelete="CASCADE",
    )
    op.drop_constraint(
        "fk_formgrpaccess_project_id_collgroup", "formgrpaccess", type_="foreignkey"
    )
    op.create_foreign_key(
        op.f("fk_formgrpaccess_project_id_collgroup"),
        "formgrpaccess",
        "collgroup",
        ["project_id", "group_id"],
        ["project_id", "group_id"],
        ondelete="CASCADE",
    )
    op.add_column(
        "fsuser", sa.Column("user_email", sa.Unicode(length=120), nullable=True)
    )
    op.drop_constraint(
        "fk_sepitems_section_project_sepsection", "sepitems", type_="foreignkey"
    )
    op.create_foreign_key(
        op.f("fk_sepitems_section_project_sepsection"),
        "sepitems",
        "sepsection",
        ["section_project", "section_form", "section_table", "section_id"],
        ["project_id", "form_id", "table_name", "section_id"],
        ondelete="CASCADE",
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        op.f("fk_sepitems_section_project_sepsection"), "sepitems", type_="foreignkey"
    )
    op.create_foreign_key(
        "fk_sepitems_section_project_sepsection",
        "sepitems",
        "sepsection",
        ["section_project", "section_form", "section_table", "section_id"],
        ["project_id", "form_id", "table_name", "section_id"],
    )
    op.drop_column("fsuser", "user_email")
    op.drop_constraint(
        op.f("fk_formgrpaccess_project_id_collgroup"),
        "formgrpaccess",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "fk_formgrpaccess_project_id_collgroup",
        "formgrpaccess",
        "collgroup",
        ["project_id", "group_id"],
        ["project_id", "group_id"],
    )
    op.drop_constraint(
        op.f("fk_formaccess_project_id_collaborator"), "formaccess", type_="foreignkey"
    )
    op.create_foreign_key(
        "fk_formaccess_project_id_collaborator",
        "formaccess",
        "collaborator",
        ["project_id", "coll_id"],
        ["project_id", "coll_id"],
    )
    op.drop_constraint(
        op.f("fk_collingroup_project_id_collgroup"), "collingroup", type_="foreignkey"
    )
    op.create_foreign_key(
        "fk_collingroup_project_id_collgroup",
        "collingroup",
        "collgroup",
        ["project_id", "group_id"],
        ["project_id", "group_id"],
    )
    op.drop_constraint(
        op.f("fk_collaborator_samas_project_collaborator"),
        "collaborator",
        type_="foreignkey",
    )
    op.create_foreign_key(
        "fk_collaborator_samas_project_collaborator",
        "collaborator",
        "collaborator",
        ["samas_project", "sameas_coll"],
        ["project_id", "coll_id"],
    )
    # ### end Alembic commands ###
