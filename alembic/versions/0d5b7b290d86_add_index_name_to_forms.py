"""Add index name to forms

Revision ID: 0d5b7b290d86
Revises: 389ebd4096fc
Create Date: 2020-04-20 15:08:24.264749

"""
from alembic import op
import sqlalchemy as sa
from alembic import context
from sqlalchemy.orm.session import Session
from pyramid.paster import get_appsettings, setup_logging
from formshare.models.formshare import Odkform, Project, Userproject
from formshare.processes.elasticsearch.repository_index import create_connection


# revision identifiers, used by Alembic.
revision = "0d5b7b290d86"
down_revision = "389ebd4096fc"
branch_labels = None
depends_on = None


def upgrade():
    config_uri = context.config.get_main_option("formshare.ini.file", None)
    if config_uri is None:
        print(
            "This migration needs parameter 'formshare.ini.file' in the alembic ini file."
        )
        print(
            "The parameter 'formshare.ini.file' must point to the full path of the FormShare ini file"
        )
        exit(1)

    setup_logging(config_uri)
    settings = get_appsettings(config_uri, "formshare")
    es_connection = create_connection(settings)
    if es_connection is None:
        print("Cannot connect to ElasticSearch")
        exit(1)

    op.add_column("odkform", sa.Column("form_index", sa.UnicodeText(), nullable=True))
    # ### end Alembic commands ###
    session = Session(bind=op.get_bind())
    forms = session.query(Odkform.project_id, Odkform.form_id).all()
    fixed = False
    for a_form in forms:
        project_code = (
            session.query(Project.project_code)
            .filter(Project.project_id == a_form.project_id)
            .first()
        )
        project_owner = (
            session.query(Userproject.user_id)
            .filter(Userproject.project_id == a_form.project_id)
            .filter(Userproject.access_type == 1)
            .first()
        )
        index_name = (
            project_owner.user_id.lower()
            + "_"
            + project_code.project_code.lower()
            + "_"
            + a_form.form_id.lower()
        )
        session.query(Odkform).filter(
            Odkform.project_id == a_form.project_id
        ).filter(Odkform.form_id == a_form.form_id).update(
            {"form_index": index_name}
        )
        fixed = True
        if es_connection.indices.exists(index_name):
            es_connection.indices.put_mapping(
                {"properties": {"_geolocation": {"type": "geo_point"}}},
                index_name,
                "dataset",
            )
    if fixed:
        session.commit()


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("odkform", "form_index")
    # ### end Alembic commands ###
