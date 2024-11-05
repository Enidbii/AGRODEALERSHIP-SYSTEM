import json


def get_request_data(request):
    if request.method == "GET":
        try:
            data_dict = json.loads(request.body)
        except Exception:
            data_dict = request.body
        return data_dict
    elif request.method == "POST":
        try:
            data_dict = json.loads(request.body)
        except Exception:
            data_dict = request.body
        return data_dict
    elif request.method == "PUT":
        try:
            data_dict = json.loads(request.body)
        except Exception as e:
            print(e)
            return None
        return data_dict



def missing_required_fields(data, required_fields):
    data_keys = list(data.keys())
    for field in required_fields:
        if field not in data_keys:
            return True
    return False
