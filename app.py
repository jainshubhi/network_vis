'''
Network Vis Main App File
'''

import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


################################# Config #######################################
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
# Database Config
db = SQLAlchemy(app)
from models import Graph

################################# Routes #######################################
@app.route('/')
def index():
    return 'Hello Graph Vis!'

@app.route('/<graph_name>')
def load_graph(graph_name):
    return 'You have just loaded %s!' % graph_name

if __name__ == '__main__':
    app.run()
