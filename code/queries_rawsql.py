import psycopg2
import pandas as pd
from marshmallow import Schema, fields, validates, validate, post_load, ValidationError
import logging
from flask_init import db_obj

log = logging.getLogger('pythonLogger') # This handler comes from config>logger.conf

def get_all_films():
    try:
        query = '''
        SELECT * FROM film
        '''
        log.debug(query)
        film_df = pd.read_sql(query, db_obj.session.bind)
        return film_df
    except psycopg2.DatabaseError as error:
        log.error(f'get_all_film_df: {error.pgcode}, {error}')
        raise RuntimeError('DB Processing Error: ' + str(error))


'''To validate the input parameters'''
def some_custom_check(data):
    '''can be replaced with customized check'''
    if not data:
        raise ValidationError('some_custom_check for title failed')
class TitleSchema(Schema):
    '''https://marshmallow.readthedocs.io/en/stable/marshmallow.validate.html'''
    title = fields.Str(required=True, validate=[validate.Length(min=1, max=50), some_custom_check])


def get_film_info(request):
    try:
        title_schema_obj = TitleSchema()
        title_schema_obj.load(request.args)
        # verification passed, hence code comes here else it would have gone to exception
        title = request.args['title']

        query = '''
        SELECT * FROM film
        WHERE title = %(title)s
        '''
        log.debug(query)
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
        title_schema_obj = TitleSchema()
        title_schema_obj.load(request.args)
        # verification passed, hence code comes here else it would have gone to exception
        title = request.args['title']

        query = '''
        SELECT a.first_name, a.last_name FROM actor a 
        INNER JOIN film_actor fa on fa.actor_id = a.actor_id 
        INNER JOIN film f on f.film_id = fa.film_id 
        WHERE f.title = %(title)s
        '''
        log.debug(query)
        actor_df = pd.read_sql(sql=query, params={'title': title}, con=db_obj.session.bind)
        return actor_df
    except psycopg2.DatabaseError as error:
        log.error(f'get_all_film_df: {error.pgcode}, {error}')
        raise RuntimeError('DB Processing Error: ' + str(error))
    except ValidationError as error:
        log.error(f'get_all_film_df: {error}')
        raise RuntimeError('Invalid Request Parameter: ' + str(error))
