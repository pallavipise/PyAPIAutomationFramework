"""
Author : Pallavi
Objective : Create and verify by POST Requests
TC#1 - Verify the status code, Headers
TC#2 - Verify the body -->Booking ID
TC#3 - Verify the JSON schema is valid
"""

import pytest
import allure
import logging
from src.constants.apicontants import *
from src.helpers.api_wrapper import *
from src.helpers.payload_manager import *
from src.helpers.utils import *
from src.helpers.common_verification import *

booking_id = None

Logger = logging.getLogger(__name__)

class TestIntegration(object):
    @pytest.mark.TC1
    @allure.feature('TC#1 Verify create token request')
    @pytest.fixture()
    def test_create_token_request(self):
        # response = requests.post("https://restful-booker.herokuapp.com/booking", headers=headers, payload=payload)
        response = create_token(url_create_token(), headers=common_headers(), payload=payload_create_token(),
                                in_json=False)
        return response.json()["token"]
        verify_http_code(response, 200)
        verify_authtokenid(response.json()["token"])

    @pytest.mark.TC2
    @allure.feature('TC#2 Verify create booking')
    def test_create_booking(self):
        global booking_id
        global Logger
        response = post_request(url_create_booking(), headers=common_headers(), auth=None,
                                payload=payload_create_booking(), in_json=False)
        booking_id = response.json()["bookingid"]
        verify_http_code(response, 200)
        verify_key(response.json()["bookingid"])

    @pytest.mark.TC3
    @allure.feature('TC#3 Verify PUT request')
    def test_put_request(self, test_create_token_request):
        global booking_id
        response = put_data(url_update_delete_booking(booking_id),
                            headers=token_headers(test_create_token_request),
                            payload=payload_update_booking(), in_json=False)
        verify_http_code(response, 200)
        verify_authtokenid(response.json()["firstname"])

    @pytest.mark.TC4
    @allure.feature('TC#4 Verify PATCH request')
    def test_patch_request(self, test_create_token_request):
        response = patch_data(url_update_delete_booking(booking_id),
                              headers=token_headers(test_create_token_request),
                              payload=payload_partial_update(), in_json=False)
        verify_http_code(response, 200)
        verify_authtokenid(response.json()["firstname"])

    @pytest.mark.TC4
    @allure.feature('TC#5 Verify DELETE request')
    def test_delete_request(self, test_create_token_request):
        response = delete_data(url_update_delete_booking(booking_id), headers=token_headers(test_create_token_request))
        verify_http_code(response, 201)
