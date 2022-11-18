import requests


class ApiChecks:

    def __init__(self, link, data, coords=None):
        self.link = link
        self.data = data
        self.coords = coords

    def get_response(self):
        response = requests.get(self.link,
                                params=self.data)
        return response

    def should_be_ok_status(self):
        status = self.get_response().status_code
        assert status == 200, 'Incorrect code status'

    def should_be_headers(self):
        headers = self.get_response().headers
        headers_list = ['Server', 'Date', 'Content-Type', 'Transfer-Encoding', 'Connection', 'Keep-Alive',
                        'Access-Control-Allow-Origin', 'Access-Control-Allow-Methods']
        for h in headers_list:
            assert h in headers, 'Incorrect/missed headers'

    def should_be_body(self):
        body = self.get_response().text
        assert len(body) > 2, 'Missed body'

    def should_be_correct_format(self):
        headers = self.get_response().headers
        val = self.data['format']
        if 'json' in val:
            assert 'json' in headers['Content-Type'], 'Wrong format'
        else:
            assert val in headers['Content-Type'], 'Wrong format'

    def should_be_correct_coords(self):
        body = self.get_response().text
        place = ''
        for key in self.data:
            if key in ['q', 'street', 'city', 'county' 'state', 'country', 'postalcode']:
                place = self.data[key]
        for places in self.coords:
            if place in places:
                for p in places[place]:
                    assert p in body, 'Incorrect coordinates'

    def should_be_able_to_geocode(self):
        body = self.get_response().text
        assert not 'Unable to geocode' in body, 'Wrong coordinates'
