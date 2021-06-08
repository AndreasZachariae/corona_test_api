from corona_test_api.corona_test_api import app
import json

def test_hello_world():
    with app.test_client() as test_app:
        response = test_app.get("/")
        assert 200 == response.status_code

        json_object = json.loads(response.data.decode())
        assert json_object == {"response": "Hello World!"}

def test_sum():
    with app.test_client() as test_app:
        response = test_app.get("/sum/1/30")
        assert 200 == response.status_code
        assert 31 == int(response.data.decode())

def test_json_response():
    with app.test_client() as test_app:
        response = test_app.get("/json")
        assert 200 == response.status_code

        json_object = json.loads(response.data.decode())
        assert json_object == {
            'key': 'value',
            "list": [1,2,3]
        }

def test_give_input():
    with app.test_client() as test_app:
        response = test_app.get("/input?parameter1=blabla")
        assert 200 == response.status_code