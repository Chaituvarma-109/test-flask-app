import os
from wsgiref import simple_server
from flask import Flask


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    return "<h1>This is test app</h1>"


port = int(os.getenv("PORT", 5000))
if __name__ == "__main__":
    host = '0.0.0.0'
    # port = 5000
    httpd = simple_server.make_server(host, port, app)
    httpd.serve_forever()
