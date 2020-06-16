import logging
from db import queries_orm

log = logging.getLogger('pythonLogger')  # This handler comes from config>logger.conf

list_supported_functions = [
    '/',
    '/index',
    '/module/v01/functions',
    '/module/v01/functions/film_list',
    '/module/v01/functions/film_info?title=<film name>',
    '/module/v01/functions/film_actors?title=<film name>',
    '/module/v01/functions/film_list_orm',
    '/module/v01/functions/film_info_orm?title=<film name>',
    '/module/v01/functions/film_actors_orm?title=<film name>'
]
def get_all_films():
    # get your data in pandas data frame format
    df = queries_orm.get_all_films()
    # apply business logic (if any)
    return df

def get_film_info(in_request):
    # get your data in pandas data frame format
    df = queries_orm.get_film_info(in_request)
    # apply business logic (if any)
    return df

def get_film_actors(in_request):
    # get your data in pandas data frame format
    actor_df = queries_orm.get_film_actors(in_request)
    # apply business logic (if any)
    return actor_df
