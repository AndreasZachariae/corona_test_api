"""API for recording Corona test results and providing a statistic.

Todo:
    * Database integration
    * Add date to input data
"""

# import json
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from marshmallow import Schema, fields
from flask import Flask, abort, request
from corona_test_api.statistics import Statistics


class StatisticsShema(Schema):
    """Marshmallow schema for statistics type
    """
    numberOfTests = fields.Int()


spec = APISpec(
    title="Corona Test API",
    version="1.0.0",
    openapi_version="3.0.2",
    info=dict(
        description="API for recording Corona test results and providing a statistic.",
        version="1.0.0",
        contact=dict(
            email="Andreas.Zachariae@gmail.com"
        )
    ),
    servers=[
        dict(
            description="Testing",
            url="http://localhost:8080/"
        ),
        dict(
            description="Flask",
            url="http://127.0.0.1:5000/"
        )
    ],
    tags=[
        dict(
            name="testresult",
            description="Corona test results"
        ),
        dict(
            name="statistics",
            description="Corona tests statistics"
        )
    ],
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)

spec.components.schema("Statistics", schema=StatisticsShema)

app = Flask(__name__)

statistics = Statistics()


@app.route("/testresult")
def get_testresult():
    test_id = request.args.get('id', type=str)

    positive = request.args.get('positive', type=bool)
    # egal welcher string, sobald nicht leer wird er true
    # Welche Annahmen darf man treffen 0/1, true/false, True/False

    if (test_id is None) or (positive is None):
        abort(400, description="Given parameters are not valid or missing." +
              str(test_id)+str(positive))

    statistics.add_test(test_id, positive)

    # response code 201 created?
    return "new test registered" + str(test_id)+str(positive)


@app.route("/statistics")
def get_statistics():
    return (statistics.get_statistics(), 200)


# with app.test_request_context():
#     spec.path(view=get_testresult)
#     spec.path(view=get_statistics)

# with open('specification.json', 'w') as f:
#     json.dump(spec.to_dict(), f)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
