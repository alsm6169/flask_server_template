import marshmallow as ma

from flask_init import db_obj


# DB sample source: https://www.postgresqltutorial.com/postgresql-sample-database/
class Actor(db_obj.Model):
    __tablename__ = 'actor'
    actor_id = db_obj.Column(db_obj.Integer, primary_key=True)
    first_name = db_obj.Column(db_obj.String(50))
    last_name = db_obj.Column(db_obj.String(120))
    last_update = db_obj.Column(db_obj.DateTime)

class ActorSchema(ma.Schema):
    class Meta:
        fields = ("actor_id", "first_name", "last_name")
        # fields = ("actor_id", "first_name", "last_name", "last_update")
        # exclude = ("last_update")


class Film(db_obj.Model):
    __tablename__ = 'film'
    film_id = db_obj.Column(db_obj.Integer, primary_key=True)
    title = db_obj.Column(db_obj.String(255), nullable=False)
    description = db_obj.Column(db_obj.String(255))
    release_year = db_obj.Column(db_obj.Integer)
    language_id = db_obj.Column(db_obj.Integer, nullable=False)
    rental_duration = db_obj.Column(db_obj.Integer, nullable=False)
    rental_rate = db_obj.Column(db_obj.Float, nullable=False)
    length = db_obj.Column(db_obj.Integer)
    replacement_cost = db_obj.Column(db_obj.Float, nullable=False)
    rating = db_obj.Column(db_obj.String(50))
    last_update = db_obj.Column(db_obj.DateTime)
    special_features = db_obj.Column(db_obj.String(255))
    fulltext = db_obj.Column(db_obj.String(255), nullable=False)
