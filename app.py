import argparse
import os
from flask import Flask
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from routes import number_written


APP = Flask(__name__)


SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Desafio Técnico"
    }
)
APP.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
APP.register_blueprint(number_written.get_blueprint())


if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(description="Technical Challenge")
    PARSER.add_argument('--debug', action='store_true', help="Use flask debug/dev mode with file change reloading")
    ARGS = PARSER.parse_args()
    PORT = int(os.environ.get('PORT', 5000))

    APP.run(host='0.0.0.0', port=PORT, debug=False)
    if ARGS.debug:
        CORS = CORS(APP)
        APP.run(host='0.0.0.0', port=PORT, debug=True)
