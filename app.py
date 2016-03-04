'''
Network Vis Main App File
'''

from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Graph Vis!'

@app.route('/<graph_name>')
def load_graph(graph_name):
    return 'You have just loaded %s!' % graph_name

if __name__ == '__main__':
    app.run()
