from functools import wraps


def validate_fields(receive_json=dict, model_json=dict, response_json=dict) -> dict:
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            missing = list()
            for key in receive_json.keys():
                if isinstance(receive_json[key], dict):
                    for i in receive_json[key].keys():
                        if i not in model_json[key]:
                            missing.append(i)
                if key not in model_json:
                    missing.append(key)
            if missing:
                response_json.update({'aux': missing})
                return response_json
            return fn(*args, **kwargs)
        return wrapper
    return decorator


def validate_fields_types(receive_json=dict, model_json=dict, response_json=dict) -> dict:
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            wrong_types = list()
            for type_field in receive_json.keys():
                if isinstance(receive_json[type_field], dict):
                    for i in receive_json[type_field].keys():
                        if type(receive_json[type_field][i]) != model_json[type_field][i]:
                            wrong_types.append(i)
                elif type(receive_json[type_field]) != model_json[type_field]:
                    wrong_types.append(type_field)
            if wrong_types:
                response_json.update({'aux': {k: str(v) for k, v in model_json.items()}})
                return response_json
            return fn(*args, **kwargs)
        return wrapper
    return decorator


def validate_json(receive_json=dict, model_json=dict, response_json_field=dict, response_json_field_type=dict) -> dict:
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            missing = list()
            for key in receive_json.keys():
                if isinstance(receive_json[key], dict):
                    for i in receive_json[key].keys():
                        if i not in model_json[key]:
                            missing.append(i)
                if key not in model_json:
                    missing.append(key)
            if missing:
                response_json_field.update({'aux': missing})
                return response_json_field

            wrong_types = list()
            for type_field in receive_json.keys():
                if isinstance(receive_json[type_field], dict):
                    for i in receive_json[type_field].keys():
                        if type(receive_json[type_field][i]) != model_json[type_field][i]:
                            wrong_types.append(i)
                elif type(receive_json[type_field]) != model_json[type_field]:
                    wrong_types.append(type_field)
            if wrong_types:
                response_json_field_type.update({'aux': {k: str(v) for k, v in model_json.items()}})
                return response_json_field_type
            return fn(*args, **kwargs)
        return wrapper
    return decorator

