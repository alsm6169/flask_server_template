import psycopg2
import pandas as pd
from marshmallow import Schema, fields, validates, validate, post_load, ValidationError

from flask_init import db_obj
from db_orm import Actor, ActorSchema

def get_all_actors_df():
    try:
        actor_df = pd.read_sql(db_obj.session.query(Actor).statement, db_obj.session.bind)
        # print(actor_df.shape)
        # print(actor_df.head())
        return actor_df
    except psycopg2.DatabaseError as error:
        print(f'get_all_film_df: {error.pgcode}, {error}')
        raise RuntimeError('DB Processing Error: ' + str(error))
    except ValidationError as error:
        print(f'get_all_film_df: {error}')
        raise RuntimeError('Invalid Request Parameter: ' + str(error))


def get_all_actors_json():
    try:
        actors = Actor.query.all()
        # for actor in actors:
        #     print('actor.last_name: ', actor.last_name, ', actor.first_name: ', actor.first_name)
        # return actors
        actor_schema_obj = ActorSchema(many = True)
        result = actor_schema_obj.dump(actors)
        # print('result: ', result)
        return result
    except psycopg2.DatabaseError as error:
        print(f'get_all_film_df: {error.pgcode}, {error}')
        raise RuntimeError('DB Processing Error: ' + str(error))
    except ValidationError as error:
        print(f'get_all_film_df: {error}')
        raise RuntimeError('Invalid Request Parameter: ' + str(error))


def get_all_film_df():
    try:
        query = '''
        SELECT * FROM film
        '''
        film_df = pd.read_sql(query, db_obj.session.bind)
        # print(film_df.shape)
        # print (film_df.head ())
        return film_df
    except psycopg2.DatabaseError as error:
        print(f'get_all_film_df: {error.pgcode}, {error}')
        raise RuntimeError('DB Processing Error: ' + str(error))
    except ValidationError as error:
        print(f'get_all_film_df: {error}')
        raise RuntimeError('Invalid Request Parameter: ' + str(error))


# use this style if there are many parameters
# class FilmInput:
#     def __init__(self, film_name):
#         self.film_name = film_name

'''To validate the input parameters'''
def some_custom_check(data):
    '''can be replaced with customized check'''
    if not data:
        raise ValidationError('some_custom_check for title failed')
class TitleSchema(Schema):
    '''https://marshmallow.readthedocs.io/en/stable/marshmallow.validate.html'''
    title = fields.Str(required=True, validate=[validate.Length(min=1, max=50), some_custom_check])


    # use this style if there are many parameters, uncomment FilmInput above
    # @post_load
    # def create_film_input_obj(self, data, **kwargs):
    #    return FilmInput(**data)

def get_film_info_df(request):
    try:
        title_schema_obj = TitleSchema()
        # use this style if there are many parameters
        # film_in_obj = title_schema_obj.load(request.args)
        title_schema_obj.load(request.args)
        # verification passed, hence code comes here else it would have gone to exception
        title = request.args['title']

        query = '''
        SELECT * FROM film
        WHERE title = %(title)s
        '''
        actor_df = pd.read_sql(sql=query, params={'title': title}, con=db_obj.session.bind)
        # print(actor_df.shape)
        # print (actor_df.head ())
        return actor_df
    except psycopg2.DatabaseError as error:
        print(f'get_all_film_df: {error.pgcode}, {error}')
        raise RuntimeError('DB Processing Error: ' + str(error))
    except ValidationError as error:
        print(f'get_all_film_df: {error}')
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
        actor_df = pd.read_sql(sql=query, params={'title': title}, con=db_obj.session.bind)
        # print(actor_df.shape)
        # print (actor_df.head ())
        return actor_df
    except psycopg2.DatabaseError as error:
        print(f'get_all_film_df: {error.pgcode}, {error}')
        raise RuntimeError('DB Processing Error: ' + str(error))
    except ValidationError as error:
        print(f'get_all_film_df: {error}')
        raise RuntimeError('Invalid Request Parameter: ' + str(error))


