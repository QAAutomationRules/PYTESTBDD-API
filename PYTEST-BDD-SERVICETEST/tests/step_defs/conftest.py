import pytest

from pytest_bdd import scenarios, given, when, then
from approvaltests.approvals import verify
from approvaltests.reporters.generic_diff_reporter_factory import GenericDiffReporterFactory

# Constants

Github_BASE_API = 'https://api.github.com'


# Hooks

def pytest_bdd_before_scenario(request, feature, scenario):
     print('Before Scenario')

def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print('Step failed: {step}')

# Fixtures



# Shared Given Steps
