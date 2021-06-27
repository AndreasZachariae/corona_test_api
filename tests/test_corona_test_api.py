"""Module for testing the corona test API
"""

import json
from corona_test_api.corona_test_api import app


def test_get_testresult():
    """Tests if adding a test result with example data returns with OK value
    """

    with app.test_client() as test_app:
        response = test_app.get("/testresult?id=1&positive=1")
        assert response.status_code == 200

    with app.test_client() as test_app:
        response = test_app.get("/testresult?id=1")
        assert response.status_code == 400


def test_get_statistics():
    """Tests for correct statistics after adding the example test before
    """

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

# test statistics separate?
