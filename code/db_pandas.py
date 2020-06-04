import psycopg2
import pandas as pd


from flask_init import db_obj


# DB sample source: https://www.postgresqltutorial.com/postgresql-sample-database/

def get_all_actors_df():
    try:
        query = '''
        select first_name, last_name from actor
        '''
        actor_df = pd.read_sql(query, db_obj.session.bind)
        # print(actor_df.shape)
        # print (actor_df.head ())
        return actor_df
    except psycopg2.DatabaseError as error:
        print(f'get_all_actors: {error.pgcode}, {error}')
