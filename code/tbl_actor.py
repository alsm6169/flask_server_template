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


