# corona_test_api
[![coverage](https://gitlab.com/hs-karlsruhe/ss2021/zaan1018/corona_test_api/badges/master/coverage.svg)](https://hs-karlsruhe.gitlab.io/ss2021/zaan1018/corona_test_api/test/)
[![markdownlint](https://hs-karlsruhe.gitlab.io/ss2021/zaan1018/corona_test_api/badges/markdownlint.svg)](https://gitlab.com/hs-karlsruhe/ss2021/zaan1018/corona_test_api/commits/master)
[![yamllint](https://hs-karlsruhe.gitlab.io/ss2021/zaan1018/corona_test_api/badges/yamllint.svg)](https://gitlab.com/hs-karlsruhe/ss2021/zaan1018/corona_test_api/commits/master)
[![pylint](https://hs-karlsruhe.gitlab.io/ss2021/zaan1018/corona_test_api/badges/pylint.svg)](https://hs-karlsruhe.gitlab.io/ss2021/zaan1018/corona_test_api/lint/)

API for recording Corona test results and providing statistics.

This API provides one route for adding new test results to the database and one route to get statistics for all registered tests.

- `/testresult` with query parameter `id` and `postive`
- `/statistics` returns json data
    ```json
    {
        "numberOfTests": int,
        "numberOfNegativeTests": int,
        "numberOfPositiveTests": int,
        "numberOfUniquePersons": int
    }
    ```

## Prerequisites

1. Install Python 3 [Download](https://www.python.org/downloads/)

1. Install Git [Instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

1. Install virtual environment pipenv
    ```bash
    pip install pipenv
    ```

## How to setup

1. Clone this project repository 
    ```bash
    git clone https://gitlab.com/hs-karlsruhe/ss2021/zaan1018/corona_test_api.git
    ```
1. Change into project directory
    ```bash
    cd corona_test_api
    ```
1. Create virtual environment with pipenv
    ```bash
    pipenv --python 3
    ```
1. Install runtime dependecies from Pipfile
    ```bash
    pipenv install
    ```

## How to run

1. Activate pipenv in GitBash
    ```bash
    pipenv shell
    ```

1. Give path to flask app
    ```bash
    export FLASK_APP=corona_test_api/corona_test_api.py
    ```

1. Start flask webserver 
    ```bash
    flask run
    ```

## How to use

The specification of the API according to OpenAPI (Swagger) OA3 can be found here:
```bash
openapi/specification.yaml
```

- path `/testresult` with GET-method
    ```yaml
    summary: "Register a new test result"
    parameters:
        - in: "query"
        name: "id"
        description: "Unique ID of a person."
        required: true
        schema:
            type: "string"
        - in: "query"
        name: "positive"
        description: "Whether test result is positive or negative."
        required: true
        schema:
            type: "boolean"
    ```

- path `/statistics` with GET-method
    ```yaml
    summary: "Test result statistics for all registered test results"
    responses:
        "200":
          description: "Successful operation"
          content:
            application/json:
              schema:
                properties:
                    numberOfTests:
                        type: "integer"
                        format: "int64"
                        description: "Total number of tests"
                    numberOfNegativeTests:
                        type: "integer"
                        format: "int64"
                        description: "Total number of negative tests"
                    numberOfPositiveTests:
                        type: "integer"
                        format: "int64"
                        description: "Total number of positive tests"
                    numberOfUniquePersons:
                        type: "integer"
                        format: "int64"
                        description: "Total"
    ```


Use `curl` for testing
```bash
curl http://localhost:5000/testresult?id=1&positive=0
curl http://localhost:5000/statistics
```

## How to contribute

### Follow the git-workflow

1. Create new local feature branch
    ```bash
    git checkout -b new-feature
    ```
1. Do your commits
    ```bash
    git add --all
    git commit -m "message"
    ```
1. Push feature branch to remote repo
    ```bash
    git push --set-upstream origin new-feature
    ```
1. Create new pull request online in GitLab

### Golden rules of writing commit messages

1. IN ENGLISH
1. Separate the subject from the body with a blank line
1. Your commit message should not contain any whitespace errors
1. Remove unnecessary punctuation marks
1. Do not end the subject line with a period
1. Capitalize the subject line and each paragraph
1. Use the imperative mood in the subject line
1. Use the body to explain what changes you have made and why you made them.
1. Do not assume the reviewer understands what the original problem was, ensure you add it.
1. Do not think your code is self-explanatory
1. Follow the commit convention defined by your team


### Linting and testing
```bash
pylint corona_test_api
pytest
pytest --cov corona_test_api
yamllint .
```

## ToDo

- [ ] Evaluate True/false from input string 
- [ ] Add API specification
- [x] Finish dev docs
- [ ] Database integration
- [ ] Add date to input data