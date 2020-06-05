import psycopg2
import pandas as pd
from marshmallow import Schema, fields, validate, post_load, ValidationError

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
        select * from film
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
class FilmInputSchema(Schema):
    '''https://marshmallow.readthedocs.io/en/stable/marshmallow.validate.html'''
    title = fields.Str(required=True)

    # use this style if there are many parameters, uncomment FilmInput above
    # @post_load
    # def create_film_input_obj(self, data, **kwargs):
    #    return FilmInput(**data)

def get_film_info_df(request):
    try:
        film_input_schema_obj = FilmInputSchema()
        # use this style if there are many parameters
        # film_in_obj = film_input_schema_obj.load(request.args)
        film_input_schema_obj.load(request.args)
        # verification passed, hence code comes here else it would have gone to exception
        title = request.args['title']

        query = '''
        select * from film
        where title = %(title)s
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


