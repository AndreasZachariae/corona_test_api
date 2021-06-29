"""Module for storing the test data
"""


class Statistics():
    """Object for storing the test data

    Stores all tests in a list of dictionaries.
    Provides functions to add new test data and get statistics about all stored tests.
    """

    def __init__(self):
        self.number_of_positive_tests = 0
        self.number_of_unique_persons = 0
        self.test_db = []

    def add_test(self, test_id: str, positive: bool):
        """Add new test data to the "database"

        Args:
            test_id (str): ID of the tested person
            positive (bool): Result of the test
        """

        if all(test["id"] != test_id for test in self.test_db):
            self.number_of_unique_persons += 1

        if positive:
            self.number_of_positive_tests += 1

        self.test_db.append({"id": test_id, "result": positive})

    def get_statistics(self):
        """Get statistics about all registered tests

        Returns:
            dictionary: Dictionary with keys for statistic values
        """
        return {"numberOfTests": len(self.test_db),
                "numberOfNegativeTests": len(self.test_db) - self.number_of_positive_tests,
                "numberOfPositiveTests": self.number_of_positive_tests,
                "numberOfUniquePersons": self.number_of_unique_persons}
