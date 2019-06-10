from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/")
def hello():
    return 'Hi from root'

@app.route('/connector/<conn>/add')
def createCon(conn):
    return conn

if __name__ == "__main__":
    app.run()
