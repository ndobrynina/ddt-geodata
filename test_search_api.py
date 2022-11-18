import pytest

from api.api_checks import ApiChecks


class TestSearchApi:

    # В файле содержатся как валидные проверки для строки, так и для именных параметров
    def test_valid_search_requests(self, valid_search_data, correct_coords):
        link = 'https://nominatim.openstreetmap.org/search?'
        search_api = ApiChecks(link, valid_search_data, correct_coords)
        search_api.get_response()
        search_api.should_be_ok_status()
        search_api.should_be_headers()
        search_api.should_be_body()
        search_api.should_be_correct_format()
        search_api.should_be_correct_coords()

    @pytest.mark.xfail
    def test_invalid_search_requests(self, invalid_search_data):
        link = 'https://nominatim.openstreetmap.org/search?'
        search_api = ApiChecks(link, invalid_search_data)
        search_api.get_response()
        search_api.should_be_ok_status()
        search_api.should_be_headers()
        search_api.should_be_body()
        search_api.should_be_correct_format()
