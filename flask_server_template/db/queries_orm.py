import psycopg2
import logging
import pandas as pd
from marshmallow import ValidationError

from db.db_extensions import db_obj, metadata, Base
# from flask_server_template import db_obj
from db.request_validator import TitleValidator

log = logging.getLogger('pythonLogger') # This handler comes from config>logger.conf


def orm_init():
    log.info('Binding metadata and reflecting the database')
    # IMPORTANT: Before first call to bind metadata to active db engine
    # see flask_routes.py @routes.before_app_first_request
    metadata.bind = db_obj.engine
    # Optional - BEGIN
    # we can reflect it ourselves from a database, using options
    # metadata.reflect(extend_existing=True,autoload_replace=True)
    # such as 'only' to limit what tables we look at...or reflect views also
    # metadata.reflect(only=['film', 'actor'], views=True, extend_existing=True, autoload_replace=True)
    # Optional - END
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
