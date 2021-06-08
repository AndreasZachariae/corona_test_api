# corona_test_api
[![coverage](https://gitlab.com/hs-karlsruhe/ss2021/zaan1018/corona_test_api/badges/master/coverage.svg)](https://hs-karlsruhe.gitlab.io/ss2021/zaan1018/corona_test_api/test/)
[![markdownlint](https://hs-karlsruhe.gitlab.io/ss2021/zaan1018/corona_test_api/badges/markdownlint.svg)](https://gitlab.com/hs-karlsruhe/ss2021/zaan1018/corona_test_api/commits/master)
[![yamllint](https://hs-karlsruhe.gitlab.io/ss2021/zaan1018/corona_test_api/badges/yamllint.svg)](https://gitlab.com/hs-karlsruhe/ss2021/zaan1018/corona_test_api/commits/master)
[![pylint](https://hs-karlsruhe.gitlab.io/ss2021/zaan1018/corona_test_api/badges/pylint.svg)](https://hs-karlsruhe.gitlab.io/ss2021/zaan1018/corona_test_api/lint/)
[![dockerlint](https://hs-karlsruhe.gitlab.io/ss2021/zaan1018/corona_test_api/badges/dockerlint.svg)](https://gitlab.com/hs-karlsruhe/ss2021/zaan1018/corona_test_api/commits/master)

API for recording Corona test results and providing a statistic.

## Golden rules of writing commit messages

0. IN ENGLISH
1. Separate the subject from the body with a blank line
2. Your commit message should not contain any whitespace errors
3. Remove unnecessary punctuation marks
4. Do not end the subject line with a period
5. Capitalize the subject line and each paragraph
6. Use the imperative mood in the subject line
7. Use the body to explain what changes you have made and why you made them.
8. Do not assume the reviewer understands what the original problem was, ensure you add it.
9. Do not think your code is self-explanatory
10. Follow the commit convention defined by your team

## Create virtual env

    pipenv --version
    pipenv --python 3
    pipenv shell
    pipenv install <name-of-package>
    pipenv install --dev

## Linting and Testing

    pylint corona_test_api
    pytest
    pytest --cov corona_test_api

## Webservice

    pipenv shell
    $env:FLASK_APP = ".\corona_test_api\corona_test_api.py"
    flask run
    curl http://127.0.0.1:5000/

## Docs
    pipenv install --dev sphinx
    cd ./docs
    sphinx-quickstart
    pipenv install --dev sphinx_rtd_theme
    conf-py -> html_theme: sphinx_rtd_theme
    conf.py -> extensions: "sphinx.ext.autodoc"
    sphinx-build . _build