from jsonmix.validate import validate_json
from examples_jsons.valid_json import EJMV_001, EJRV_001, EJCERT_001, ESJMV_001, ESJRV_001

# EJRV = example json receive valid
# EJMV = example json model valid
# ESJRV = example strong json receive valid
# ESJMV = example strong json model valid
# EJCERT = example json custom error response types
# EJCERF = example json custom error response fields


def test_validate_type_valid():
    sort = dict
    got = [
        type(validate_json(receive=EJRV_001, model=EJMV_001, response_field_type=EJCERT_001, operation='types')),
        type(validate_json(receive=ESJRV_001, model=ESJMV_001, response_field_type=EJCERT_001, operation='types'))
    ]
    for item in got:
        assert verification_condition((item != sort)) is True


def verification_condition(condition):
    if condition is True:
        return True
    else:
        return False
