import os
from flask import Flask, request
from werkzeug.exceptions import BadRequest

from function import create_response

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')


@app.route('/perform_query')
def perform_query():
    try:
        cmd1 = request.args['cmd1']
        cmd2 = request.args['cmd2']
        value1 = request.args['value1']
        value2 = request.args['value2']
        file_name = request.args['file_name']
    except KeyError:
        raise BadRequest

    file_path = os.path.join(DATA_DIR, file_name)
    if not os.path.exists(file_path):
        return BadRequest(description='File is not found')

    with open(file_path) as f:
        result = create_response(f, cmd1, value1)
        result = create_response(result, cmd2, value2)
        content = '\n'.join(result)

    return app.response_class(content, content_type='text/plain')
