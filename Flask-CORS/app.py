from flask import Flask, render_template
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


def create_app(test_config=None):
    app = Flask(__name__)
#   CORS(app)
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PATCH,POST,DELETE,OPTIONS')
        return response

    @app.route('/messages')
    @cross_origin()
    def get_messages():
        return 'GETTING MESSAGES'
