from datetime import datetime

# EJRI = example json receive invalid
# EJMV = example json model valid
# ESJRI = example strong json receive invalid
# ESJMV = example strong json model valid
# EJCERT = example json custom error response types
# EJCERF = example json custom error response fields

EJRI_001 = {
    'uid': '1',
    'Na': 'Json Mix',
    'Vesion': '0.1.0',
    'message': 'A library for validate in python'
}
EJRI_002 = {
    'uid': '1',
    'Name': 'Json Mix',
    'Version': '0.1.0',
    'message': 'A library for validate in python',
    'add_field': 'test'
}
EJRI_003 = {
    'uid': '1',
    'Name': 'Json Mix',
    'add_field': 'test',
    'Version': '0.1.0',
    'message': 'A library for validate in python'
}
EJRI_004 = {
    'uid': '1',
    'Name': 'Json Mix',
    'Version': '0.1.0',
    'message': 'A library for validate in python'
}
EJRI_005 = {
    'uid': '1',
    'Name': 'Json Mix',
    'Version': 0.1,
    'message': 'A library for validate in python'
}
ESJRI_001 = {
    'uid': '1',
    'data': {
        'Na': 'Json Mix',
        'Version': '0.1.0',
        'message': 'A library for validate in python'
    },
    'date': str(datetime.now().timestamp())
}
ESJRI_002 = {
    'uid': '1',
    'data': {
        'Name': 'Json Mix',
        'Version': '0.1.0',
        'message': 'A library for validate in python'
    },
    'date': datetime.now().timestamp()
}
ESJRI_003 = {
    'uid': '1',
    'data': {
        'Nam': 'Json Mix',
        'Version': '0.1.0',
        'message': 'A library for validate in python'
    },
    'date': datetime.now().timestamp()
}
ESJMV_001 = {
    'uid': int,
    'data': {
        'Name': str,
        'Version': str,
        'message': str
    },
    'date': str
}
EJMV_001 = {
    'uid': int,
    'Name': str,
    'Version': str,
    'message': str
}
EJCERF_001 = {
    "code": "JMERR-001",
    "data": {
        "error": "inconsistency on JSON structure",
        "message": "Missing required JSON field",
    },
    "date": str(datetime.now().timestamp()),
}
EJCERT_001 = {
    "code": "JMERR-002",
    "data": {
        "error": "inconsistency on JSON structure",
        "message": "JSON field type is incorrect"
    },
    "date": str(datetime.now().timestamp())
}
