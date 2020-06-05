from flask import jsonify, make_response, request
from flask import current_app as app
from marshmallow import ValidationError

import db_queries


@app.errorhandler(404)
def not_found(error):
    """Page not found."""
    return make_response(jsonify({'Error': 'URL NOT FOUND'}, 404))


@app.errorhandler(400)
def bad_request():
    """Bad request."""
    return make_response(jsonify({'Error': 'BAD REQUEST'}, 400))

@app.route('/module/v01/functions/actor_list_alchemy_df', methods=['GET'])
def get_actor_list_alchemy_df():
    try:
        print('inside get_actor_list_alchemy_df')
        actor_df = db_queries.get_all_actors_df()
        response_code = 200
        response_msg = actor_df.to_json(orient='records')
    except ValidationError as err:
        response_code = err.code
        response_msg = jsonify(err.messages)
    except RuntimeError as err:
        response_code = err.code
        response_msg = jsonify(err.messages)
    return make_response(response_msg, response_code)


@app.route('/module/v01/functions/actor_list_alchemy_json', methods=['GET'])
def get_actor_list_alchemy_json():
    try:
        print('inside get_actor_list_alchemy_json')
        actors = db_queries.get_all_actors_json()
        response_code = 200
        # response_msg = jsonify({'STATUS' : 'WORKED INTERNALLY'})
        response_msg = jsonify(actors)
    except ValidationError as err:
        response_code = err.code
        response_msg = jsonify(err.messages)
    except RuntimeError as err:
        response_code = err.code
        response_msg = jsonify(err.messages)
    return make_response(response_msg, response_code)

@app.route('/module/v01/functions/film_list_rawsql_df', methods=['GET'])
def get_film_list_rawsql_df():
    try:
        print('inside get_film_list_rawsql_df')
        actor_df = db_queries.get_all_film_df()
        response_code = 200
        response_msg = actor_df.to_json(orient='records')
    except ValidationError as err:
        response_code = err.code
        response_msg = jsonify(err.messages)
    except RuntimeError as err:
        response_code = err.code
        response_msg = jsonify(err.messages)
    return make_response(response_msg, response_code)

@app.route('/module/v01/functions/film_actor_rawsql_df', methods=['GET'])
def get_film_actors_rawsql_df():
    try:
        print('inside get_film_actors_rawsql_df')
        actor_df = db_queries.get_film_actors_df(request.args)
        response_code = 200
        response_msg = actor_df.to_json(orient='records')
    except ValidationError as err:
        response_code = err.code
        response_msg = jsonify(err.messages)
    except RuntimeError as err:
        response_code = err.code
        response_msg = jsonify(err.messages)
    return make_response(response_msg, response_code)
