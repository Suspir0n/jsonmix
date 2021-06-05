from datetime import datetime

# EJRV = example json receive valid
# EJMV = example json model valid
# ESJRV = example strong json receive valid
# ESJMV = example strong json model valid
# EJCERT = example json custom error response types
# EJCERF = example json custom error response fields

EJRV_001 = {
    'uid': 1,
    'Name': 'Json Mix',
    'Version': '0.1.0',
    'message': 'A library for validate in python'
}
EJMV_001 = {
    'uid': int,
    'Name': str,
    'Version': str,
    'message': str
}
ESJRV_001 = {
    'uid': 1,
    'data': {
        'Name': 'Json Mix',
        'Version': '0.1.0',
        'message': 'A library for validate in python'
    },
    'date': str(datetime.now().timestamp())
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
EJCERT_001 = {
    "code": "JMERR-002",
    "data": {
        "error": "inconsistency on JSON structure",
        "message": "JSON field type is incorrect"
    },
    "date": str(datetime.now().timestamp())
}
EJCERF_001 = {
    "code": "JMERR-001",
    "data": {
        "error": "inconsistency on JSON structure",
        "message": "Missing required JSON field"
    },
    "date": str(datetime.now().timestamp()),
}