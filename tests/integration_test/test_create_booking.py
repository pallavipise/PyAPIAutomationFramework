"""
Author : Pallavi
Objective : Create and verify by POST Requests
TC#1 - Verify the status code, Headers
TC#2 - Verify the body -->Booking ID
TC#3 - Verify the JSON schema is valid
"""

import pytest
from src.constants.apicontants import url_create_booking
from src.constants.apicontants import url_create_token
from src.helpers.api_wrapper import post_request, create_token
from src.helpers.payload_manager import payload_create_booking, payload_create_token
from src.helpers.utils import common_headers
from src.helpers.common_verification import *


class TestIntegration(object):
    def test_create_booking_tc1(self):
        response = post_request(url_create_booking(), headers=common_headers(), auth=None,
                                payload=payload_create_booking(), in_json=False)
        verify_http_code(response, 200)
        verify_key(response.json()["bookingid"])

    # def test_create_token_request(self):
    #     # response = requests.post("https://restful-booker.herokuapp.com/booking", headers=headers, payload=payload)
    #     response = create_token(url_create_token(), headers=common_headers(), payload=payload_create_token(), in_json=False)
    #     verify_http_code(response, 200)
    #     verify_key(response.json()["token"])

    # def test_create_booking_tc2(self):
    #      assert True == False
    #
    #
    #
    # def test_create_booking_tc3(self):
    #      assert True == True
