'''
Network Vis Main App File
'''

from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Graph Vis!'

if __name__ == '__main__':
    app.run()
