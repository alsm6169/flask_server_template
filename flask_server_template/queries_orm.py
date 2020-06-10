from sqlalchemy.ext.automap import automap_base
import psycopg2
import logging
import pandas as pd
from marshmallow import ValidationError
from sqlalchemy import MetaData

from flask_server_template import db_obj
from request_validator import TitleValidator

log = logging.getLogger('pythonLogger') # This handler comes from config>logger.conf

# https://docs.sqlalchemy.org/en/13/orm/extensions/automap.html
# https://www.youtube.com/watch?v=UK57IHzSh8I
# produce our own MetaData object
metadata = MetaData(bind=db_obj.engine) # here a parameter called schema can be used if we want to reflect only particular db schema

# Optional - BEGIN
# we can reflect it ourselves from a database, using options
metadata.reflect(extend_existing=True,autoload_replace=True)
# such as 'only' to limit what tables we look at...or reflect views also
# metadata.reflect(only=['film', 'actor'], views=True, extend_existing=True, autoload_replace=True)
# Optional - END

# we can then produce a set of mappings from this MetaData.
Base = automap_base(metadata=metadata)
# calling prepare() just sets up mapped classes and relationships
Base.prepare(db_obj.engine, reflect=True)

def get_all_films():
    try:
        film_orm = Base.classes.film
        # result_set = db_obj.session.query(film_orm).all()
        # for r in result_set:
        #     print(r.title)
        qry = db_obj.session.query(film_orm)
        log.debug('query> ' + str(qry.statement))
        film_df = pd.read_sql(qry.statement, db_obj.session.bind)
        return film_df
    except psycopg2.DatabaseError as error:
        log.error(f'get_all_film_df: {error.pgcode}, {error}')
        raise RuntimeError('DB Processing Error: ' + str(error))


def get_film_info(request):
    try:
        title_schema_obj = TitleValidator()
        title_schema_obj.load(request.args)
        # verification passed, hence flask_server_template comes here else it would have gone to exception
        title = request.args['title']
        film_orm = Base.classes.film
        qry = db_obj.session.query(film_orm).\
            filter(film_orm.title == title)
        log.debug('query> ' + str(qry.statement) + ', title> ' + title)
        film_df = pd.read_sql(qry.statement, db_obj.session.bind)
        return film_df
    except psycopg2.DatabaseError as error:
        log.error(f'get_all_film_df: {error.pgcode}, {error}')
        raise RuntimeError('DB Processing Error: ' + str(error))
    except ValidationError as error:
        log.error(f'get_all_film_df: {error}')
        raise RuntimeError('Invalid Request Parameter: ' + str(error))


def get_film_actors(request):
    try:
        title_schema_obj = TitleValidator()
        title_schema_obj.load(request.args)
        # verification passed, hence flask_server_template comes here else it would have gone to exception
        title = request.args['title']
        log.debug('title: ' + title)
        film_orm = Base.classes.film
        actor_orm = Base.classes.actor
        film_actor_orm = Base.classes.film_actor
        # https://docs.sqlalchemy.org/en/13/orm/tutorial.html#querying-with-joins
        # https://stackoverflow.com/questions/53531826/in-sqlalchemy-what-is-the-difference-between-the-filter-vs-join-and-filter-s
        qry = db_obj.session.query(actor_orm).\
            join(film_actor_orm,film_orm).\
            filter(film_orm.title == title)
        log.debug('query> ' + str(qry.statement) + ', title> ' + title)
        actor_df = pd.read_sql(qry.statement, db_obj.session.bind)
        return actor_df
    except psycopg2.DatabaseError as error:
        log.error(f'get_all_film_df: {error.pgcode}, {error}')
        raise RuntimeError('DB Processing Error: ' + str(error))
    except ValidationError as error:
        log.error(f'get_all_film_df: {error}')
        raise RuntimeError('Invalid Request Parameter: ' + str(error))
