from flask import jsonify, make_response, request
from flask import current_app as app

import logging

# log = logging.getLogger(__name__)
log = logging.getLogger('pythonLogger')  # This handler comes from config>logger.conf

import queries_rawsql
import queries_orm


@app.errorhandler(404)
def not_found(error):
    """Page not found."""
    return make_response(jsonify({'Error': 'URL NOT FOUND'}, 404))


@app.errorhandler(400)
def bad_request():
    """Bad request."""
    return make_response(jsonify({'Error': 'BAD REQUEST'}, 400))


'''RAW SQL based queries - BEGIN'''
@app.route('/module/v01/functions/film_list', methods=['GET'])
def get_film_list():
    try:
        log.debug('inside get_film_list')
        df = queries_rawsql.get_all_films()
        response_code = 200
        response_msg = df.to_json(orient='records')
    except RuntimeError as err:
        response_code = 700  # err.code
        response_msg = jsonify(str(err))
    return make_response(response_msg, response_code)


@app.route('/module/v01/functions/film_info', methods=['GET'])
def get_film_info():
    try:
        log.debug('inside get_film_info')
        df = queries_rawsql.get_film_info(request)
        response_code = 200
        response_msg = df.to_json(orient='records')
    except RuntimeError as err:
        response_code = 700  # err.code
        response_msg = jsonify(str(err))
    return make_response(response_msg, response_code)


@app.route('/module/v01/functions/film_actors', methods=['GET'])
def get_film_actors():
    try:
        log.debug('inside get_film_actors')
        actor_df = queries_rawsql.get_film_actors(request)
        response_code = 200
        response_msg = actor_df.to_json(orient='records')
    except RuntimeError as err:
        response_code = 700  # err.code
        response_msg = jsonify(str(err))
    return make_response(response_msg, response_code)

'''RAW SQL based queries - END'''

'''ORM Object based queries - BEGIN'''
@app.route('/module/v01/functions/film_list_orm', methods=['GET'])
def get_film_list_orm():
    try:
        log.debug('inside get_film_list_orm')
        film_df = queries_orm.get_all_films()
        response_code = 200
        response_msg = film_df.to_json(orient='index')
        # response_msg = jsonify({'Status': 'All good!'})
    except RuntimeError as err:
        response_code = 700  # err.code
        response_msg = jsonify(str(err))
    return make_response(response_msg, response_code)

@app.route('/module/v01/functions/film_info_orm', methods=['GET'])
def get_film_info_orm():
    try:
        log.debug('inside get_film_info_orm')
        film_df = queries_orm.get_film_info(request)
        response_code = 200
        response_msg = film_df.to_json(orient='index')
    except RuntimeError as err:
        response_code = 700  # err.code
        response_msg = jsonify(str(err))
    return make_response(response_msg, response_code)


@app.route('/module/v01/functions/film_actors_orm', methods=['GET'])
def get_film_actors_orm():
    try:
        log.debug('inside get_film_actors_orm')
        actor_df = queries_orm.get_film_actors(request)
        response_code = 200
        response_msg = actor_df.to_json(orient='index')
    except RuntimeError as err:
        response_code = 700  # err.code
        response_msg = jsonify(str(err))
    return make_response(response_msg, response_code)
'''ORM Object based queries - END'''