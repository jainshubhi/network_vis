'''
Network Vis Models
'''

from app import db
from sqlalchemy.dialects.postgresql import JSON


class Graph(db.Model):
    __tablename__ = 'graphs'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)
    graph_json = db.Column(JSON)

    def __repr__(self):
        return '<id> {}, <url> {}'.format(id, url)
