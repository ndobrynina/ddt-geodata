import pytest

from dataset.get_data import get_data_from_file, get_data_from_json


@pytest.fixture(scope="function", params=get_data_from_file('dataset/valid_search_data.csv'))
def valid_search_data(request):
    yield request.param


@pytest.fixture()
def correct_coords():
    coord_dict = get_data_from_json('dataset/correct_coords.json')
    return coord_dict


@pytest.fixture(scope="function", params=get_data_from_json('dataset/invalid_search_data.json'))
def invalid_search_data(request):
    yield request.param


@pytest.fixture(scope="function", params=get_data_from_file('dataset/valid_reverse_data.csv'))
def valid_reverse_data(request):
    yield request.param

@pytest.fixture(scope="function", params=get_data_from_json('dataset/invalid_reverse_data.json'))
def invalid_reverse_data(request):
    yield request.param