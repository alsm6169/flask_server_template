from flask import jsonify, make_response, request
from flask import current_app as app

import logging
# log = logging.getLogger(__name__)
log = logging.getLogger('pythonLogger') # This handler comes from config>logger.conf

import db_queries


@app.errorhandler(404)
def not_found(error):
    """Page not found."""
    return make_response(jsonify({'Error': 'URL NOT FOUND'}, 404))


@app.errorhandler(400)
def bad_request():
    """Bad request."""
    return make_response(jsonify({'Error': 'BAD REQUEST'}, 400))

@app.route('/module/v01/functions/film_list', methods=['GET'])
def get_film_list():
    try:
        log.debug('inside get_film_list')
        actor_df = db_queries.get_all_films()
        response_code = 200
        response_msg = actor_df.to_json(orient='records')
    except RuntimeError as err:
        response_code = 700  # err.code
        response_msg = jsonify(str(err))
    return make_response(response_msg, response_code)

@app.route('/module/v01/functions/film_info', methods=['GET'])
def get_film_info():
    try:
        log.debug('inside get_film_info')
        actor_df = db_queries.get_film_info(request)
        response_code = 200
        response_msg = actor_df.to_json(orient='records')
    except RuntimeError as err:
        response_code = 700 # err.code
        response_msg = jsonify(str(err))
    return make_response(response_msg, response_code)

@app.route('/module/v01/functions/film_actors', methods=['GET'])
def get_film_actors():
    try:
        log.debug('inside get_film_actors')
        actor_df = db_queries.get_film_actors(request)
        response_code = 200
        response_msg = actor_df.to_json(orient='records')
    except RuntimeError as err:
        response_code = 700 # err.code
        response_msg = jsonify(str(err))
    return make_response(response_msg, response_code)
