from os import getenv
from os.path import exists

from flask import Flask
from flask import request

import json

from logging.config import dictConfig

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

REFERENCES_FILE = getenv("REFERENCES_FILE", "references.json")
if not exists(REFERENCES_FILE):
    raise FileNotFoundError(
        f"{REFERENCES_FILE} was not found. Please create it or set the 'REFERENCES_FILE' environment variable.")

with open(REFERENCES_FILE) as f:
    references = json.load(f)

app = Flask(__name__)


@app.route('/references/<int:guild_id>')
def index(guild_id):
    app.logger.info(f"Request for references of Guild with Id {guild_id}")
    app.logger.info(
        f"Authorization header: {request.headers.get('Authorization', '')}")

    return references


if __name__ == '__main__':
    app.run(host='0.0.0.0')
