import psycopg2
import pandas as pd

from flask_init import db_obj
from tbl_actor import Actor, ActorSchema

def get_all_actors_df():
    try:
        actor_df = pd.read_sql(db_obj.session.query(Actor).statement, db_obj.session.bind)
        # print(actor_df.shape)
        # print(actor_df.head())
        return actor_df
    except psycopg2.DatabaseError as error:
         print(f'get_all_actors: {error.pgcode}, {error}')

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
        print(f'get_all_actors: {error.pgcode}, {error}')


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

'''TODO: Work in Progress'''
def get_film_actors_df():
    try:
        query = '''
        select * from film
        '''
        actor_df = pd.read_sql(query, db_obj.session.bind)
        # print(actor_df.shape)
        # print (actor_df.head ())
        return actor_df
    except psycopg2.DatabaseError as error:
        print(f'get_all_film_df: {error.pgcode}, {error}')
