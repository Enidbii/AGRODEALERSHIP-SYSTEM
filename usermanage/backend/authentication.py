import json

from django.contrib.auth import authenticate
from django.contrib.auth.models import Group, Permission
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from usermanage.backend.utils import get_request_data, missing_required_fields
from usermanage.backend.servicebase import ServiceInterface
from usermanage.models import OtherUser, Corporate, State


# def create_group(request):
#     data = get_request_data(request)
#     group_name = data.get('group_name')
#     try:
#         group = ServiceInterface().create(Group, group_name=group_name)
#         group.save()
#         return JsonResponse({"code": "200.000.000", "message": "Group created"})
#     except Exception as e:
#         print(e)
#         return JsonResponse({"code": "403.000.000", "message": "Group created"})

class AuthenticateUser(object):
    @csrf_exempt
    def register(self, request):
        data = get_request_data(request)
        print(data)
        first_name = data.get("first_name")
        print(first_name)
        last_name = data.get("last_name")
        email = data.get("email")
        email = email.lower()
        username = data.get("username")
        password = data.get("password")
        phone_number = data.get("phone_number")
        groups = data.get("groups")
        
        required_fields = ['first_name', 'last_name', 'email', 'username', 'password', 'phone_number', 'groups']

        if missing_required_fields(data, required_fields):
            return JsonResponse({"code": "404.000", "message": "You are missing some required fields"})
        else:
            try:
                user = ServiceInterface().create(OtherUser, first_name=first_name, last_name=last_name, email=email,
                                  username=username, phone_number=phone_number)
                my_group = Group.objects.get(name=groups)
                user.groups.add(my_group)
                user.set_password(password)
                user.save()
                print(user.id)
                return JsonResponse({"code": "200.000", "message": "User successfully created"})
            except Exception as e:
                print(e)
                return {"code": "404.000.000", "message": "User could not be created"}



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
        print(data)
        first_name = data.get("first_name")
        print(first_name)
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        password = data.get("password")
        phone_number = data.get("phone_number")
        if not OtherUser.id:
            return JsonResponse({"code": "202.000.000", "message": "The user_id does not exist"})
        try:
            user = OtherUser.objects.get(username=username)
            print(user.id)
            print(user.group)
            updated = ServiceInterface().update(OtherUser, instance_id=user.id, first_name=first_name, email=email, last_name=last_name,
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

        required_fields = ['name', 'description', 'Alias']

        if missing_required_fields(data, required_fields):
            return JsonResponse({"code": "404.000", "message": "Missing the required fields"})

        try:
            corporate = ServiceInterface().create(Corporate, name=name, description=description, alias=alias)
            corporate.save()
            return JsonResponse({"code": "200.000.000", "message":"Corporate successfully created!"})

        except Exception as e:
            print(e)
            return JsonResponse({"code": "404.000.000", "message": "Corporate creation unsuccessful"})

    def add_state(self, request):
        data = get_request_data(request)
        print(data)
        name = data.get("name")
        description = data.get("description")
        print(name, description)

        required_fields = ['name', 'description']

        if missing_required_fields(data, required_fields):
            return JsonResponse({"code": "404.000", "message": "Missing the required fields"})
        try:
            state = ServiceInterface().create(State, name=name, description=description)
            state.save()
            return JsonResponse({"code": "200.000.000", "message": "State successfully created!"})

        except Exception as e:
            print(e)
            return JsonResponse({"code": "404.000.000", "message": "State creation unsuccessful"})

    def delete_user(self, request):
        data = get_request_data(request)
        print(data)
        username = data.get("username")
        user = OtherUser.objects.get(username=username)
        print(user.id)
        try:
            ServiceInterface().delete(OtherUser, instance_id=user.id)
            return JsonResponse({"code": "200.000.000", "message": "User deleted!!!!"})
        except Exception as e:
            print(e)
            return JsonResponse({"code": "404.000.000", "message": "User could not be deleted"})


    def update_corporate(self, request):
        data = get_request_data(request)
        print(data)
        name = data.get("name")
        Alias = data.get("Alias")
        description = data.get("description")
        corporate = Corporate.objects.get(alias=Alias)
        print(corporate.alias)
        if not corporate.id:
            return JsonResponse({"code": "202.000.000", "message": "The user_id does not exist"})
        try:
            updated = ServiceInterface().update(Corporate, instance_id=corporate.id, name=name, description=description)
            updated.save()
            return JsonResponse({"code": "200.000.000", "message": "Updated successfully"})
        except Exception as e:
            print(e)
            return JsonResponse({"code": "404.000.000", "message": "Could not be updated successfully"})

    def get_records(self):
        try:
            ServiceInterface().retrieve_all_records(OtherUser)
            OtherUser.objects.values()
            return JsonResponse({"code": "200", "message": "success"})
        except Exception as e:
            print(e)
            return JsonResponse({"code": "403", "message": "failed"})

    def create_group(self, request):
        data = get_request_data(request)
        name = data.get('name')
        permissions = data.get('permissions')
        try:
           #new_group ,created = Group.objects.get_or_create(name='new_group')
           ServiceInterface().create(Group, name=name)

           return JsonResponse({"code": "200", "message": "Success"})

        except Exception as e:
            print(e)
            return JsonResponse({"code": "403", "message": "Failed"})










