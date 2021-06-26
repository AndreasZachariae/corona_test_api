class Statistics(object):
    def __init__(self):
        self.number_of_positive_tests = 0
        self.number_of_unique_persons = 0
        self.test_db = []

    def add_test(self, id: str, positive: bool):

        if all(test["id"] != id for test in self.test_db):
            self.number_of_unique_persons += 1

        if positive:
            self.number_of_positive_tests += 1

        self.test_db.append({"id": id, "result": positive})

    def get_statistics(self):
        return {"numberOfTests": len(self.test_db),
                "numberOfNegativeTests": len(self.test_db) - self.number_of_positive_tests,
                "numberOfPositiveTests": self.number_of_positive_tests,
                "numberOfUniquePersons": self.number_of_unique_persons}
