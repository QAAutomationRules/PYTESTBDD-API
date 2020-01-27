"""
This module contains step definitions for githubservice.feature.
It uses the requests package:
http://docs.python-requests.org/
"""

import requests, pytest, json, uuid
from pytest_bdd import scenario, scenarios, given, when, then, parsers
from approvaltests.approvals import verify
from faker import Faker


# Shared Variables

GitHub_API = 'https://api.github.com'
User_Resource = '/user'
User_Repos_Resource = '/user/repos'
url = 'https://api.github.com/users/KTJ-Demo'
user = 'KTJ-Demo'
password = 'Dog.Bone1'
faker = Faker()
name = uuid.uuid4().hex
description = faker.words(8)

# Scenarios

scenarios('../features/githubservice.feature')


# Given Steps

@given('the user executes a GET User call')
def gh_given_response():
    response = requests.get(GitHub_API + User_Resource, auth=(user, password)) 
    return response

@given('the user Creates a new GitHub Repository')
def gh_post_response():
    
    payload = {
        'name': name,
        'description': description,
        'homepage': 'https://github.com',
        'private': False,
        'has_issues': True,
        'has_projects': True,
        'has_wiki': True,
        'is_template': False,
        'auto_init': True,
        'gitignore_template': 'VisualStudio',
        'license_template': 'mit',
        'allow_squash_merge': True,
        'allow_merge_commit': True,
        'allow_rebase_merge': True
    }
    print(payload)
    response = requests.post(GitHub_API + User_Repos_Resource, auth=(user, password), data=json.dumps(payload) ) 
    return response

# When Steps

#@when('')
#def gh_response():
#   print("When")

# Then Steps

@then('the user receives a response with the correct github project details')
def test_gh_response_content(gh_given_response):
    #remove the public repos key from the dictionary
    data = gh_given_response.json()
    data.pop('public_repos')
    data.pop('disk_usage')
    data.pop('updated_at')
    jsonResult = json.dumps(data, indent=4)
    print(jsonResult)
    verify(jsonResult)

@then(parsers.parse('the response status code is "{code:d}"'))
def gh_response_code(gh_given_response, code):
    assert gh_given_response.status_code == code    

@then('the github repository is created in the system')
def test_gh_response_content(gh_post_response):
    print(gh_post_response.json())
    assert gh_post_response.status_code == 201
    assert gh_post_response.json()['name'] == name
    
    
