# corona_test_api
[![coverage](https://gitlab.com/hs-karlsruhe/ss2021/zaan1018/corona_test_api/badges/master/coverage.svg)](https://hs-karlsruhe.gitlab.io/ss2021/zaan1018/corona_test_api/test/)
[![markdownlint](https://hs-karlsruhe.gitlab.io/ss2021/zaan1018/corona_test_api/badges/markdownlint.svg)](https://gitlab.com/hs-karlsruhe/ss2021/zaan1018/corona_test_api/commits/master)
[![yamllint](https://hs-karlsruhe.gitlab.io/ss2021/zaan1018/corona_test_api/badges/yamllint.svg)](https://gitlab.com/hs-karlsruhe/ss2021/zaan1018/corona_test_api/commits/master)
[![pylint](https://hs-karlsruhe.gitlab.io/ss2021/zaan1018/corona_test_api/badges/pylint.svg)](https://hs-karlsruhe.gitlab.io/ss2021/zaan1018/corona_test_api/lint/)
[![dockerlint](https://hs-karlsruhe.gitlab.io/ss2021/zaan1018/corona_test_api/badges/dockerlint.svg)](https://gitlab.com/hs-karlsruhe/ss2021/zaan1018/corona_test_api/commits/master)

API for recording Corona test results and providing a statistic.

## Golden rules of writing commit messages

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

## Create virtual env
```bash
pipenv --version
pipenv --python 3
pipenv shell
pipenv install <name-of-package>
pipenv install --dev
```
## Linting and Testing
```bash
pylint corona_test_api
pytest
pytest --cov corona_test_api
yamllint .
```
## Webservice
```bash
pipenv shell
$env:FLASK_APP = ".\corona_test_api\corona_test_api.py" #Powershell
export FLASK_APP=corona_test_api/corona_test_api.py #GitBash
export FLASK_ENV=development
flask run

curl http://127.0.0.1:5000/

curl http://127.0.0.1:5000/testresult?id=1&positive=0

curl http://127.0.0.1:5000/statistics
```
## Docs
```bash
pipenv install --dev sphinx
pipenv install --dev sphinx_rtd_theme

cd ./docs
sphinx-quickstart
```
conf.py -> html_theme: sphinx_rtd_theme

conf.py -> extensions: "sphinx.ext.autodoc"
```bash
sphinx-build . _build
```
### Markdown
```bash
pip install --upgrade myst-parser
extensions = ['myst_parser']
```