import json
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from usermanage.backend.userservice import ServiceInterface
from usermanage.models import OtherUser


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
            data_dict = request.body
        return data_dict



def missing_required_fields(data, required_fields):
    data_keys = list(data.keys())
    for field in required_fields:
        if field not in data_keys:
            return True
    return False

class AuthenticateUser(object):
    @csrf_exempt
    def register(self, request):
        data = get_request_data(request)
        print(data)
        first_name = data.get("first_name")
        print(first_name)
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        password = data.get("password")
        phone_number = data.get("phone_number")
        required_fields = ['first_name', 'last_name', 'email', 'username', 'password', 'phone_number']

        if missing_required_fields(data, required_fields):
            return {"code": "404.000", "message": "You are missing some required fields"}
        else:
            try:
                user = ServiceInterface().get(OtherUser, first_name=first_name, last_name=last_name, email=email,
                                  username=username, phone_number=phone_number)
                user.set_password(password)
                user.save()
                return JsonResponse({"code": "200.000", "message": "User successfully created"})
            except Exception as e:
                print(e)
                return {"code": "404.000.000", "message": "User not created"}



    def login(self, request):
        data = get_request_data(request)
        print(data)
        username = data.get('username')
        password = data.get('password')
        required_fields = ['username', 'password']
        if missing_required_fields(data, required_fields):
            return JsonResponse({"code": "404.000", "message": "You are missing some required fields"})

        user = authenticate(username=username, password=password)
        if user is not None:
            return JsonResponse({"code": "200.000", "message": "You've logged in successfully"}, status=200)
        else:
            return JsonResponse({"code": "404.001", "message": "User not found"}, status=404)

    def update(self, request):
        data = get_request_data(request)
        username = data.get('username')
        user_id = data.get('id')
        if not username:
            return JsonResponse({"code": "202.000.000", "message": "The username is incorrect"})
        update = ServiceInterface().update(OtherUser,instance_id=user_id, username=username)
        update.save()
        return JsonResponse({"code": "200.000.000", "message": "Username updated successfully"})



