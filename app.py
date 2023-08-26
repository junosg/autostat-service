# app.py
from flask import Flask, request
from flask_cors import CORS
from werkzeug.middleware.proxy_fix import ProxyFix
from src.Controllers.TestController import test_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(test_bp)

@app.route("/")
def hello_world():
    return "<h1>Starter Flask App</h1>"

if __name__ == '__main__':
    app.wsgi_app = ProxyFix(
        app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
    )

    app.run(debug=True, host='0.0.0.0')