import json
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from marshmallow import Schema, fields
from flask import Flask, abort, request, make_response, jsonify
from corona_test_api.statistics import Statistics


class StatisticsShema(Schema):
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
    id = request.args.get('id', type=str)

    positive = request.args.get('positive', type=bool)
    # egal welcher string, sobald nicht leer wird er true
    # Welche Annahmen darf man treffen 0/1, true/false, True/False

    if (id is None) or (positive is None):
        abort(400, description="Given parameters are not valid or missing." +
              str(id)+str(positive))

    statistics.add_test(id, positive)

    # response code 201 created?
    return ("new test registered" + str(id)+str(positive))


@app.route("/statistics")
def get_statistics():
    return (statistics.get_statistics(), 200)


@app.route("/")
def hello_world():
    """ Hello World!
    ---
    get:
        description: Hello World!
        responses:
            200:
                description: Succesfully helloed to world!
                content:
                    text/plain:
                        schema:
                            type: string
                            example: Hello World!
    """
    return {"response": "Hello World!"}


@app.route("/sum/<int:number1>/<int:number2>")
def sum(number1, number2):
    """Sum of two integers
    ---
    get:
        description: Sum of two integers
        parameters:
            - in: path
              name: number1
              description: First number to add
              required: true
              schema:
                type: integer
            - in: path
              name: number2
              description: Second number to add
              required: true
              schema:
                type: integer
        responses:
            200:
                description: Succesfully added both numbers!
    """
    return str(number1 + number2)


@app.route("/json")
def json_response():
    return {
        'key': 'value',
        "list": [1, 2, 3]
    }


@app.route("/input")
def give_input():
    parameter1 = request.args.get("parameter1")
    return(parameter1)


with app.test_request_context():
    spec.path(view=hello_world)
    spec.path(view=sum)

with open('specification.json', 'w') as f:
    json.dump(spec.to_dict(), f)

#import yaml
# with open('specification.yml', 'w') as f:
#    yaml.dump(spec.to_yaml(), f)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
