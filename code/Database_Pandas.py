from sqlalchemy import create_engine
import sqlalchemy as db
import psycopg2

import os
import GlobalValues
import pandas as pd


def get_con_str():
    # Example: 'postgresql://scott:tiger@localhost:5432/mydatabase'
    # db_con_str = f'postgresql://' \
    #              f'{GlobalValues.run_conf_data["DB_USER"]}' \
    #              f'@' \
    #              f'{GlobalValues.run_conf_data["DB_SERVER"]}:' \
    #              f'{GlobalValues.run_conf_data["DB_PORT"]}/' \
    #              f'{GlobalValues.run_conf_data["DB_NAME"]}'
    pwd = os.getenv ('DB_PWD')  # get password from environment variable DB_PWD
    db_con_str = f'postgresql://' \
                 f'{GlobalValues.run_conf_data["DB_USER"]}:' \
                 f'{pwd}@' \
                 f'{GlobalValues.run_conf_data["DB_SERVER"]}:' \
                 f'{GlobalValues.run_conf_data["DB_PORT"]}/' \
                 f'{GlobalValues.run_conf_data["DB_NAME"]}'
    return db_con_str


def get_all_actors():
    db_con_str = get_con_str ()
    db_engine = create_engine (db_con_str)  # , echo=True)

    try:
        with db_engine.connect () as conn:
            metadata = db.MetaData ()
            actor = db.Table ('actor', metadata, autoload=True, autoload_with=db_engine)
            query = db.select ([actor])
            res = conn.execute (query)
            print (res.fetchall ())

    except psycopg2.DatabaseError as error:
        print (f'get_all_actors: {error.pgcode}, {error}')


def get_all_actors_df():
    db_con_str = get_con_str ()
    db_engine = create_engine (db_con_str, echo=True)

    try:
        with db_engine.connect () as conn:
            query = '''
            select first_name, last_name from actor
            '''
            actor_df = pd.read_sql (con=conn, sql=query)
            print (actor_df.shape)
            # print (actor_df.head ())
            return actor_df

    except psycopg2.DatabaseError as error:
        print (f'get_all_actors: {error.pgcode}, {error}')
