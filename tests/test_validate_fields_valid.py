from jsonmix.validate import validate_fields
from datetime import datetime


example_json_receive_valid = {
    'uid': '1',
    'Name': 'Json Mix',
    'Version': '0.1.0',
    'message': 'A library for validate in python'
}
example_json_model_valid = {
    'uid': int,
    'Name': str,
    'Version': str,
    'message': str
}
example_strong_json_receive_valid = {
    'uid': 1,
    'data': {
        'Name': 'Json Mix',
        'Version': '0.1.0',
        'message': 'A library for validate in python'
    },
    'date': str(datetime.now().timestamp())
}
example_strong_json_model_valid = {
    'uid': int,
    'data': {
        'Name': str,
        'Version': str,
        'message': str
    },
    'date': str
}
example_json_custom_error_response = {
    "code": "JMERR-001",
    "data": {
        "error": "inconsistency on JSON structure",
        "message": "Missing required JSON field"
    },
    "date": str(datetime.now().timestamp()),
}



def test_validate_json_valid():
    @validate_fields(receive_json=example_json_receive_valid, model_json=example_json_model_valid,
                     response_json=example_json_custom_error_response)
    def validate_one_field_simple_valid():
        message = 'Olá Mundo'
        return message
    message_one = validate_one_field_simple_valid()
    assert verification_condition((type(message_one) != dict)) is True

    @validate_fields(receive_json=example_strong_json_receive_valid, model_json=example_strong_json_model_valid,
                     response_json=example_json_custom_error_response)
    def validate_field_strong_valid():
        message = 'Olá Mundo'
        return message
    message_strong = validate_field_strong_valid()
    assert verification_condition((type(message_strong) != dict)) is True


def verification_condition(condition):
    if condition is True:
        return True
    else:
        return False
