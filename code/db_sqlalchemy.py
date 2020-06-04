import psycopg2
import pandas as pd
import marshmallow as ma

from flask_init import db_obj

# DB sample source: https://www.postgresqltutorial.com/postgresql-sample-database/
class Actor(db_obj.Model):
    __tablename__ = 'actor'
    actor_id = db_obj.Column(db_obj.Integer, primary_key=True)
    first_name = db_obj.Column(db_obj.String(50))
    last_name = db_obj.Column(db_obj.String(120))
    last_update = db_obj.Column(db_obj.DateTime)

    def __init__(self, first_name=None, last_name=None):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return '<User %r>' % (self.first_name)

class ActorSchema(ma.Schema):
    class Meta:
        fields = ("actor_id", "first_name", "last_name")
        # fields = ("actor_id", "first_name", "last_name", "last_update")
        # exclude = ("last_update")


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
