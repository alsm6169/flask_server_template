import psycopg2
import pandas as pd
from marshmallow import ValidationError
import logging
from flask_server_template import db_obj
from db.request_validator import TitleValidator

log = logging.getLogger('pythonLogger') # This handler comes from config>logger.conf

def get_all_films():
    try:
        query = '''
        SELECT * FROM film
        '''
        log.debug('query> ' + query)
        film_df = pd.read_sql(query, db_obj.session.bind)
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

        query = '''
        SELECT * FROM film
        WHERE title = %(title)s
        '''

        log.debug('query> ' + query + ', title> ' + title)
        actor_df = pd.read_sql(sql=query, params={'title': title}, con=db_obj.session.bind)
        return actor_df
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

        query = '''
        SELECT a.first_name, a.last_name FROM actor a 
        INNER JOIN film_actor fa on fa.actor_id = a.actor_id 
        INNER JOIN film f on f.film_id = fa.film_id 
        WHERE f.title = %(title)s
        '''
        log.debug('query> ' + query + ', title> ' + title)
        actor_df = pd.read_sql(sql=query, params={'title': title}, con=db_obj.session.bind)
        return actor_df
    except psycopg2.DatabaseError as error:
        log.error(f'get_all_film_df: {error.pgcode}, {error}')
        raise RuntimeError('DB Processing Error: ' + str(error))
    except ValidationError as error:
        log.error(f'get_all_film_df: {error}')
        raise RuntimeError('Invalid Request Parameter: ' + str(error))
