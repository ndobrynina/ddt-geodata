import pytest

from api.api_checks import ApiChecks


class TestReverseApi:

    # В координатах прописаны экстремумы Земли, за исключением Антарктиды
    @pytest.mark.parametrize('coords',
                             [{'lat': 83.6176068, 'lon': -31.3320566}, {'lat': -54.9446686, 'lon': -66.1728416},
                              {'lat': 8.1850089, 'lon': 30.091299}, {'lat': 52.8765224, 'lon': 172.3770741},
                              {'lat': -9.9586417, 'lon': -150.2503602}])
    def test_valid_reverse_requests(self, coords, valid_reverse_data):
        link = f"https://nominatim.openstreetmap.org/reverse?lat={coords['lat']}&lon={coords['lon']}&"
        search_api = ApiChecks(link, valid_reverse_data)
        search_api.get_response()
        search_api.should_be_ok_status()
        search_api.should_be_headers()
        search_api.should_be_body()
        search_api.should_be_correct_format()
        search_api.should_be_able_to_geocode()

    @pytest.mark.xfail
    def test_invalid_reverse_requests(self, invalid_reverse_data):
        link = 'https://nominatim.openstreetmap.org/reverse?'
        search_api = ApiChecks(link, invalid_reverse_data)
        search_api.get_response()
        search_api.should_be_ok_status()
        search_api.should_be_headers()
        search_api.should_be_body()
        search_api.should_be_correct_format()
