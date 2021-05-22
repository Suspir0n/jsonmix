from functools import wraps


def validate_fields(receive_json=dict, model_json=dict, response_json=dict) -> dict:
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            missing = list()
            for key in receive_json.keys():
                if isinstance(receive_json[key], dict):
                    for i in receive_json[key].keys():
                        if receive_json[key][i] != model_json[key][i]:
                            missing.append(i)
                if key not in model_json:
                    missing.append(key)
            if missing:
                response_json.update({'aux': missing})
                return response_json
            return fn(*args, **kwargs)
        return wrapper
    return decorator
