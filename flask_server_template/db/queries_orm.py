import psycopg2
import logging
import pandas as pd

from .db_extensions import db_obj, Base

log = logging.getLogger('pythonLogger') # This handler comes from config>logger.conf


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


def get_film_info(title):
    try:
        film_orm = Base.classes.film
        qry = db_obj.session.query(film_orm).\
            filter(film_orm.title == title)
        log.debug('query> ' + str(qry.statement) + ', title> ' + title)
        film_df = pd.read_sql(qry.statement, db_obj.session.bind)
        return film_df
    except psycopg2.DatabaseError as error:
        log.error(f'get_all_film_df: {error.pgcode}, {error}')
        raise RuntimeError('DB Processing Error: ' + str(error))


def get_film_actors(title):
    try:
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
