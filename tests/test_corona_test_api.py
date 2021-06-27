import json
from corona_test_api.corona_test_api import app


def test_get_testresult():
    with app.test_client() as test_app:
        response = test_app.get("/testresult?id=1&positive=1")
        assert response.status_code == 200


def test_get_statistics():
    with app.test_client() as test_app:
        response = test_app.get("/statistics")
        assert response.status_code == 200

        json_object = json.loads(response.data.decode())
        assert json_object == {
            'numberOfTests': 1,
            "numberOfNegativeTests": 0,
            "numberOfPositiveTests": 1,
            "numberOfUniquePersons": 1
        }
