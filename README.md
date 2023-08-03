# Python API Automation Framework

## Integration Test Cases for the Restful Booker
URL = https://restful-booker.herokuapp.com/apidoc/index.html
1. Verify GET, POST, PATCH, DELETE, PUT.
2. Response Body, Headers and Status code
3. Auth - Basic Auth, Cookie based Auth.
4. JSON Schema validation

## Tech stack(Python Packages used)
1. Request Module
2. Pytest, Pytest-html
3. Allure Report
4. Faker, csv, JSON, YAML.
5. Run via commandline-Jenkins

#### P.S - DB Connection (in future)

## Install pip packages 
- ` pip install pytest pytest-html allure-pytest jsonschema `
- ` pip install requirements.txt `

## How to run locally and see the report?
'pytest tests/integration_test/test_create_booking.py -s -v --alluredir=./reports --html=report.html'

## How to run via Jenkins?