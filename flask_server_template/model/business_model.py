import logging
from marshmallow import ValidationError

from db import queries_orm
import db.queries_rawsql as qry

from .request_validator import TitleValidator

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

'''RAW SQL based queries - BEGIN'''
def get_film_info_sql(in_request):
    try:
        # validate the URL parameters
        title_schema_obj = TitleValidator()
        title_schema_obj.load(in_request.args)
        # verification passed, hence flask_server_template comes here else it would have gone to exception
        title = in_request.args['title']
        log.debug('title: ' + title)
        # get your data in pandas data frame format
        df = qry.get_film_info(title)
        # apply business logic (if any)
        return df
    except ValidationError as error:
        log.error(f'get_all_film_df: {error}')
        raise RuntimeError('Invalid Request Parameter: ' + str(error))

def get_film_actors_sql(in_request):
    try:
        # validate the URL parameters
        title_schema_obj = TitleValidator()
        title_schema_obj.load(in_request.args)
        # verification passed, hence flask_server_template comes here else it would have gone to exception
        title = in_request.args['title']
        log.debug('title: ' + title)
        # get your data in pandas data frame format
        actor_df = qry.get_film_actors(title)
        # apply business logic (if any)
        return actor_df
    except ValidationError as error:
        log.error(f'get_all_film_df: {error}')
        raise RuntimeError('Invalid Request Parameter: ' + str(error))

'''RAW SQL based queries - END'''


'''ORM Object based queries - BEGIN'''
def get_film_info_orm(in_request):
    try:
        # validate the URL parameters
        title_schema_obj = TitleValidator()
        title_schema_obj.load(in_request.args)
        # verification passed, hence flask_server_template comes here else it would have gone to exception
        title = in_request.args['title']
        log.debug('title: ' + title)
        # get your data in pandas data frame format
        df = queries_orm.get_film_info(title)
        # apply business logic (if any)
        return df
    except ValidationError as error:
        log.error(f'get_all_film_df: {error}')
        raise RuntimeError('Invalid Request Parameter: ' + str(error))

def get_film_actors_orm(in_request):
    try:
        # validate the URL parameters
        title_schema_obj = TitleValidator()
        title_schema_obj.load(in_request.args)
        # verification passed, hence flask_server_template comes here else it would have gone to exception
        title = in_request.args['title']
        log.debug('title: ' + title)
        # get your data in pandas data frame format
        actor_df = queries_orm.get_film_actors(title)
        # apply business logic (if any)
        return actor_df
    except ValidationError as error:
        log.error(f'get_all_film_df: {error}')
        raise RuntimeError('Invalid Request Parameter: ' + str(error))
'''ORM Object based queries - END'''
