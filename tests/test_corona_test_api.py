"""Module for testing the corona test API
"""

import json
from corona_test_api.corona_test_api import app


def test_get_home():
    """Tests if home path returns with OK value
    """

    with app.test_client() as test_app:
        response = test_app.get("/")
        assert response.status_code == 200


def test_get_testresult():
    """Tests if adding a test result with example data returns with OK value
    """

    with app.test_client() as test_app:
        response = test_app.get("/testresult?id=1&positive=1")
        assert response.status_code == 201
        assert response.data == b'Successful operation. Added test result for 1 with result: True'

        response = test_app.get("/testresult?id=2&positive=false")
        assert response.status_code == 201
        assert response.data == b'Successful operation. Added test result for 2 with result: False'

        response = test_app.get("/testresult?id=1")
        assert response.status_code == 400

        response = test_app.get("/testresult?id=1&positive=falsch")
        assert response.status_code == 400


def test_get_statistics():
    """Tests for correct statistics after adding the example tests before
    """

    with app.test_client() as test_app:
        response = test_app.get("/statistics")
        assert response.status_code == 200

        json_object = json.loads(response.data.decode())
        assert json_object == {
            "numberOfTests": 2,
            "numberOfNegativeTests": 1,
            "numberOfPositiveTests": 1,
            "numberOfUniquePersons": 2
        }
