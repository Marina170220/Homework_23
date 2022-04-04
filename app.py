import json
import os
from flask import Flask, request
from werkzeug.exceptions import BadRequest

from function import create_response

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')


@app.route("/perform_query", methods=["POST"])
def perform_query():
    try:
        data = json.loads(request.data)
        cmd1 = data['cmd1']
        cmd2 = data['cmd2']
        value1 = data['value1']
        value2 = data['value2']
        file_name = data['file_name']
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
