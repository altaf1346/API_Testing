import pytest
from datetime import datetime
from utils.client_api import Api
import json
import os 

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
   report_dir = 'reports'
   now = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
   config.option.htmlpath = f"{report_dir}/report_{now}.html"

@pytest.fixture(scope="session",autouse=True)
def api():
    return Api()


@pytest.fixture(scope="session")
def load_user_data():
    json_file_path = os.path.join(os.path.dirname(__file__), "data", "test_data.json")
    with open(json_file_path) as json_file:
        data = json.load(json_file)  # Load the JSON data from the json_file
    return data



