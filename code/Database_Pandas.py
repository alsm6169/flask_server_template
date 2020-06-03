from sqlalchemy import create_engine
import sqlalchemy as db
import psycopg2

import app_config
import pandas as pd


# DB sample source: https://www.postgresqltutorial.com/postgresql-sample-database/

def get_all_actors():
    db_con_str = app_config.get_db_con_str()
    db_engine = create_engine(db_con_str)  # , echo=True)

    try:
        with db_engine.connect() as conn:
            metadata = db.MetaData()
            actor = db.Table('actor', metadata, autoload=True, autoload_with=db_engine)
            query = db.select([actor])
            res = conn.execute(query)
            print(res.fetchall())

    except psycopg2.DatabaseError as error:
        print(f'get_all_actors: {error.pgcode}, {error}')


def get_all_actors_df():
    db_con_str = app_config.get_db_con_str()
    db_engine = create_engine(db_con_str, echo=True)

    try:
        with db_engine.connect() as conn:
            query = '''
            select first_name, last_name from actor
            '''
            actor_df = pd.read_sql(con=conn, sql=query)
            print(actor_df.shape)
            # print (actor_df.head ())
            return actor_df
    except psycopg2.DatabaseError as error:
        print(f'get_all_actors: {error.pgcode}, {error}')
