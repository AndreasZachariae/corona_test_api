"""API for recording Corona test results and providing a statistic.

Todo:
    * Database integration
    * Add date to input data
"""

from flask import Flask, abort, request
from flask_cors import CORS  # neccessary for swagger editor to work
from corona_test_api.statistics import Statistics

app = Flask(__name__)

cors = CORS(app)

statistics = Statistics()

# standard route "/" für home?


@app.route("/")
def home():
    """Home page with instructions how to use the API

    Returns:
        string: Instructions
        int: response code
    """
    return "Welcome to the corona test API!\n\
            Use `/ testresult` with query parameter `id` and `postive`\n\
            For statistics use `/ statistics`", 200


@app.route("/testresult")
def get_testresult():
    """Add new test result with GET-method

    Parameters are in the query string
        * id (string)
        * positive (bool)

    Returns:
        string: message
        int: response_code
    """
    test_id = request.args.get('id', type=str)

    positive = request.args.get('positive', type=str)

    if (test_id is None) or (positive is None):
        abort(400, description="Given parameters are not valid or missing." +
              str(test_id)+str(positive))

    if positive in ("true", "True", "1"):
        positive = True
    elif positive in ("false", "False", "0"):
        positive = False
    else:
        abort(400, description="Given parameters are not valid or missing." +
              str(test_id)+str(positive))

    statistics.add_test(test_id, positive)

    return ("Successful operation. Added test result for " + str(test_id) + " with result: " + str(positive), 201)


@app.route("/statistics")
def get_statistics():
    """GET-method to recieve statistics data about all tests

    Returns:
        json: statistics
    """
    return (statistics.get_statistics(), 200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
