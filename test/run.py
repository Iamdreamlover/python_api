import datetime

import flask
from flask import request, jsonify

from invalid_usage import InvalidUsage
from validation import validate_greeting

app = flask.Flask(__name__)


@app.route("/score", methods=['POST'])
def getscore() -> str:
    errors = validate_greeting(request)
    if errors is not None:
        print(errors)
        raise InvalidUsage(errors)

    content = request.get_json()
    dateFirst = str(content['date_first'])
    dateSecond = str(content['date_second'])
    channel = str(content['channel'])
    cha_num = str(content['cha_num'])
    frame = str(content['frame'])
    # print(frame)

    return jsonify(score = 123, probability = "Very hight")


# def toDate(dateString):
#     return datetime.datetime.strptime(dateString, '%Y-%m-%dT%H:%M:%S')


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


app.run(host="0.0.0.0", port=8080)
