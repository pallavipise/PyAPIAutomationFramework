def payload_create_booking():
    payload = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    }
    return payload


def payload_create_token():
    payload_token = {
        "username": "admin",
        "password": "password123"
    }
    return payload_token


def payload_update_booking():
    payload_update =  {
        "firstname": "Pallavi",
        "lastname": "Pise",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload_update

def payload_partial_update():
    payload_partialupdate =  {
        "firstname": "Akshat",
        "lastname": "Raj",
    }
    return payload_partialupdate


