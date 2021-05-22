from jsonmix.validate import validate_fields
from datetime import datetime


example_one_json_receive_valid = {
    'uid': '1',
    'Name': 'Json Mix',
    'Version': '0.1.0',
    'message': 'A library for validate in python'
}
example_one_json_model_valid = {
    'uid': int,
    'Name': str,
    'Version': str,
    'message': str
}
example_two_json_receive_valid = {
    'uid': '1',
    'data': {
        'Name': 'Json Mix',
        'Version': '0.1.0',
        'message': 'A library for validate in python'
    },
    'date': str(datetime.now().timestamp())
}
example_two_json_model_valid = {
    'uid': int,
    'data': {
        'Name': str,
        'Version': str,
        'message': str
    },
    'date': str
}
example_json_custom_error_response = {
    "code": "BSERR-001",
    "data": {
        "error": "inconsistency on JSON structure",
        "message": "Missing required JSON field",
    },
    "date": str(datetime.now().timestamp()),
}



def test_validate_json_valid():
    @validate_fields(receive_json=example_one_json_receive_valid, model_json=example_one_json_model_valid,
                     response_json=example_json_custom_error_response)
    def validate_one_field_simple_valid():
        message = 'Olá Mundo'
        return message
    message_one = validate_one_field_simple_valid()
    assert verification_condition((type(message_one) != dict)) is True

    @validate_fields(receive_json=example_one_json_receive_valid, model_json=example_two_json_model_valid,
                     response_json=example_json_custom_error_response)
    def validate_two_field_simple_valid():
        message = 'Olá Mundo'
        return message

    message_two = validate_one_field_simple_valid()
    assert verification_condition((type(message_two) != dict)) is True


def verification_condition(condition):
    if condition is True:
        return True
    else:
        return False
