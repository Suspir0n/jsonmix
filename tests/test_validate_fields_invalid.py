from jsonmix.validate import validate_json
from examples_jsons.invalid_json import EJRI_001, EJRI_002, EJRI_003, ESJRI_001, EJMV_001, ESJMV_001, EJCERF_001

# EJRI = example json receive invalid
# EJMV = example json model valid
# ESJRI = example strong json receive invalid
# ESJMV = example strong json model valid
# EJCERT = example json custom error response types
# EJCERF = example json custom error response fields


def test_validate_fields_invalid():
    sort = dict
    got = [
        type(validate_json(receive=EJRI_001, model=EJMV_001, response_field=EJCERF_001, operation='fields')),
        type(validate_json(receive=EJRI_002, model=EJMV_001, response_field=EJCERF_001, operation='fields')),
        type(validate_json(receive=EJRI_003, model=EJMV_001, response_field=EJCERF_001, operation='fields')),
        type(validate_json(receive=ESJRI_001, model=ESJMV_001, response_field=EJCERF_001, operation='fields'))
    ]
    for item in got:
        assert verification_condition((item != sort)) is False


def verification_condition(condition):
    if condition is True:
        return True
    else:
        return False
