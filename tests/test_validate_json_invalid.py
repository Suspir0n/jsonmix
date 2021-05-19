from jsonmix.validate import validate_json
from datetime import datetime


example_one_json_receive_invalid = {
    'uid': '1',
    'Na': 'Json Mix',
    'Vesion': '0.1.0',
    'message': 'A library for validate in python'
}
example_two_json_receive_invalid = {
    'uid': '1',
    'Name': 'Json Mix',
    'Version': '0.1.0',
    'message': 'A library for validate in python',
    'add_field': 'test'
}
example_three_json_receive_invalid = {
    'uid': 1,
    'Na': 'Json Mix',
    'Version': '0.1.0',
    'message': 'A library for validate in python'
}
example_json_model_valid = {
    'uid': int,
    'Name': str,
    'Version': str,
    'message': str
}
example_strong_json_receive_invalid = {
    'uid': 1,
    'data': {
        'Na': 'Json Mix',
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
example_json_custom_error_response_field = {
    "code": "JMERR-001",
    "data": {
        "error": "inconsistency on JSON structure",
        "message": "Missing required JSON field"
    },
    "date": str(datetime.now().timestamp())
}
example_json_custom_error_response_field_type = {
    "code": "JMERR-002",
    "data": {
        "error": "inconsistency on JSON structure",
        "message": "JSON field type is incorrect"
    },
    "date": str(datetime.now().timestamp())
}



def test_validate_json_invalid():
    @validate_json(receive_json=example_one_json_receive_invalid, model_json=example_json_model_valid,
                     response_json_field=example_json_custom_error_response_field, response_json_field_type=example_json_custom_error_response_field_type)
    def validate_one_json_invalid():
        message = 'Olá Mundo'
        return message
    message_one = validate_one_json_invalid()
    assert verification_condition((type(message_one) != dict)) is False

    @validate_json(receive_json=example_two_json_receive_invalid, model_json=example_json_model_valid,
                           response_json_field=example_json_custom_error_response_field, response_json_field_type=example_json_custom_error_response_field_type)
    def validate_two_json_invalid():
        message = 'Olá Mundo'
        return message

    message_two = validate_two_json_invalid()
    assert verification_condition((type(message_two) != dict)) is False

    @validate_json(receive_json=example_three_json_receive_invalid, model_json=example_json_model_valid,
                           response_json_field=example_json_custom_error_response_field, response_json_field_type=example_json_custom_error_response_field_type)
    def validate_three_json_invalid():
        message = 'Olá Mundo'
        return message

    message_two = validate_three_json_invalid()
    assert verification_condition((type(message_two) != dict)) is False

    @validate_json(receive_json=example_strong_json_receive_invalid, model_json=example_strong_json_model_valid,
                     response_json_field=example_json_custom_error_response_field, response_json_field_type=example_json_custom_error_response_field_type)
    def validate_json_strong_invalid():
        message = 'Olá Mundo'
        return message
    message_strong = validate_json_strong_invalid()
    assert verification_condition((type(message_strong) != dict)) is False


def verification_condition(condition):
    if condition is True:
        return True
    else:
        return False
