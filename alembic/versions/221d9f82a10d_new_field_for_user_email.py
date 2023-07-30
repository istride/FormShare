"""New field for user email

Revision ID: 221d9f82a10d
Revises: 4f59ec12363e
Create Date: 2021-02-23 20:53:45.850561

"""
import time

import requests
from alembic import context
from formshare.processes.elasticsearch.user_index import configure_user_index_manager
from pyramid.paster import get_appsettings, setup_logging

# revision identifiers, used by Alembic.
revision = "221d9f82a10d"
down_revision = "4f59ec12363e"
branch_labels = None
depends_on = None


def upgrade():
    new_mapping = {
        "properties": {
            "user_email": {"type": "text", "copy_to": ["all_data", "user_email2"]},
            "user_email2": {"type": "text", "analyzer": "email"},
        }
    }

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

    es_host = settings.get("elasticsearch.user.host", "localhost")
    es_port = settings.get("elasticsearch.user.port", 9200)
    use_ssl = settings.get("elasticsearch.user.use_ssl", "False")

    ready = False
    print("Waiting for ES to be ready")
    while not ready:
        if use_ssl == "False":
            resp = requests.get("http://{}:{}/_cluster/health".format(es_host, es_port))
        else:
            resp = requests.get(
                "https://{}:{}/_cluster/health".format(es_host, es_port)
            )
        data = resp.json()
        if data["status"] == "yellow" or data["status"] == "green":
            ready = True
        else:
            time.sleep(30)
    print("ES is ready")

    if use_ssl == "False":
        resp = requests.get(
            "http://{}:{}/_cat/indices?format=json".format(es_host, es_port)
        )
    else:
        resp = requests.get(
            "https://{}:{}/_cat/indices?format=json".format(es_host, es_port)
        )
    indexes = resp.json()
    user_index_found = False
    for an_index in indexes:
        if an_index["index"] == settings["elasticsearch.user.index_name"]:
            user_index_found = True

    if user_index_found:
        user_index = configure_user_index_manager(settings)
        es_connection = user_index.create_connection()
        es_connection.indices.put_mapping(
            new_mapping, index=user_index.index_name, doc_type="_doc"
        )

        if use_ssl == "False":
            r = requests.post(
                "http://{}:{}/{}/_update_by_query?conflicts=proceed".format(
                    user_index.host, user_index.port, user_index.index_name
                )
            )
        else:
            r = requests.post(
                "https://{}:{}/{}/_update_by_query?conflicts=proceed".format(
                    user_index.host, user_index.port, user_index.index_name
                )
            )
        if r.status_code != 200:
            print("Cannot update with query")
            exit(1)


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
