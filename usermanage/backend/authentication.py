import json
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import logout
from usermanage.backend.servicebase import ServiceInterface
from usermanage.models import OtherUser, Corporate


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

    def update(self, request, user_id):
        data = get_request_data(request)
        print(data)
        first_name = data.get("first_name")
        print(first_name)
        last_name = data.get("last_name")
        username = data.get("username")
        password = data.get("password")
        phone_number = data.get("phone_number")
        if not user_id:
            return JsonResponse({"code": "202.000.000", "message": "The user_id does not exist"})
        try:
            updated = ServiceInterface().update(OtherUser, instance_id=user_id,first_name=first_name, last_name=last_name,
                                               username=username, password=password, phone_number=phone_number)
            updated.save()
            return JsonResponse({"code": "200.000.000", "message": "Updated successfully"})
        except Exception as e:
            print(e)
            return JsonResponse({"code": "404.000.000", "message": "Could not be updated successfully"})


    def logout(self, request):
        try:
            ServiceInterface().logout(OtherUser)
            return JsonResponse({"code": "200.000.000", "message": "Logout successful"})
        except Exception as e:
            print(e)
            return JsonResponse({"code": "404.000.000", "message": "Logout unsuccessful"})

    def create_corporate(self, request):
        data = get_request_data(request)
        print(data)
        name = data.get("name")
        description = data.get("description")
        alias = data.get("Alias")
        print(name, description, alias)

        required_fields = ['name', 'description', 'Alias']

        if missing_required_fields(data, required_fields):
            return JsonResponse({"code": "404.000", "message": "Missing the required fields"})

        try:
            corporate = ServiceInterface().create_user(Corporate, name=name, description=description, alias=alias)
            print(type(corporate))
            corporate.save()
            return JsonResponse({"code": "200.000.000", "message":"Corporate successfully created!"})

        except Exception as e:
            print(e)
            return JsonResponse({"code": "404.000.000", "message": "Corporate creation unsuccessful"})





