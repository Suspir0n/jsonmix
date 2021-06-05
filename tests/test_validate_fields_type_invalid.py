from jsonmix.validate import validate_json
from examples_jsons.invalid_json import EJRI_004, EJRI_005, ESJRI_002, EJMV_001, ESJMV_001, EJCERT_001

# EJRI = example json receive invalid
# EJMV = example json model valid
# ESJRI = example strong json receive invalid
# ESJMV = example strong json model valid
# EJCERT = example json custom error response types
# EJCERF = example json custom error response fields


def test_validate_type_invalid():
    sort = dict
    got = [
        type(validate_json(receive=EJRI_004, model=EJMV_001, response_field_type=EJCERT_001, operation='types')),
        type(validate_json(receive=EJRI_005, model=EJMV_001, response_field_type=EJCERT_001, operation='types')),
        type(validate_json(receive=ESJRI_002, model=ESJMV_001, response_field_type=EJCERT_001, operation='types'))
    ]
    for item in got:
        assert verification_condition((item != sort)) is False


def verification_condition(condition):
    if condition is True:
        return True
    else:
        return False
