# PYTESTBDD-API
Starter project for PYTEST-BDD including Python Request Library and Approval Tests library.  Sample against Github.

To run tests with pytest-html reporting:

CD to PYTEST-BDD-SERVICETEST folder

i.e. C:\VSO\Public\PYTESTBDD-API\PYTEST-BDD-SERVICETEST>

pipenv run pytest -k "githubAPITest" --html=report.html --approvaltests-use-reporter='PythonNative'