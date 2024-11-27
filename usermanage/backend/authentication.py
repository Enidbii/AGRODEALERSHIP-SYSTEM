import base64
import json
import hashlib
from django.contrib.auth.models import Group, Permission
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import get_object_or_404

from usermanage.backend.utils import get_request_data, missing_required_fields
from usermanage.backend.servicebase import ServiceInterface
from usermanage.models import OtherUser, Corporate, State, Authorization
from django.core.management.utils import get_random_secret_key


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

def check_authorization(token, app_name):
    # data = get_request_data(request)
    # app_name = data.get('app_name')

    try:
        auth = ServiceInterface().get(Authorization, app_name=app_name)
        if auth.token == token:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False



class AuthenticateUser(object):
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
        app_name = data.get('app_name')
        token = data.get('token')
        if not check_authorization(token, app_name):
            return JsonResponse({"code": "404.000.000", "message": "Unauthorised"})
        
        required_fields = ['first_name', 'last_name', 'email', 'username', 'password', 'phone_number', 'groups', 'app_name', 'token']

        if missing_required_fields(data, required_fields):
            return JsonResponse({"code": "404.000", "message": "You are missing some required fields"})
        else:
            try:
                hashed_phone_number = hashlib.sha256(phone_number.encode()).hexdigest()
                user = ServiceInterface().create(OtherUser, first_name=first_name, last_name=last_name, email=email,
                                  username=username, phone_number=hashed_phone_number)
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

        try:
            user = OtherUser.objects.get(username=username, password=password)
            if user is not None:
                return JsonResponse({"code": "200.000", "message": "You've logged in successfully"}, status=200)
        except Exception as e:
            print(e)
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

    def read_user(self, request):
        data = get_request_data(request)
        user_id = data.get('user_id')

        try:
            user = ServiceInterface().retrieve_one_record(OtherUser, instance_id=user_id)
            queryset = user.values()
            print(queryset)
            data = json.dumps(list(queryset), cls=DjangoJSONEncoder)
            return JsonResponse({"code": "200.000.000", "data": data})
        except Exception as e:
            print(e)
            return JsonResponse({"code": "403.000.000", "message": "User not available"})




    def logout(self, request):
        try:
            ServiceInterface().logout(OtherUser)
            return JsonResponse({"code": "200.000.000", "message": "Logout successful"})
        except Exception as e:
            print(e)
            return JsonResponse({"code": "404.000.000", "message": "Logout unsuccessful"})

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

    def read_corporates(self, request):
        try:
            corporates = ServiceInterface().retrieve_all_records(Corporate)
            queryset = corporates.values()
            print(queryset)
            data = json.dumps(list(queryset), cls=DjangoJSONEncoder)
            return JsonResponse({"code": "200.000.000", "data": data})

        except Exception as e:
            print(e)
            return JsonResponse({"code": "403.000.000", "message": "Failed"})

    def delete_corporate(self, request):
        data = get_request_data(request)
        alias = data.get('alias')
        corporate = Corporate.objects.get(alias=alias)
        print(corporate.id)

        try:
            ServiceInterface().delete(Corporate, instance_id=corporate.id)
            return JsonResponse({"code": "200.000.000", "message":"Corporate successfully deleted"})
        except Exception as e:
            print(e)
            return JsonResponse({"code": "403.000.000", "message": "Failed"})

    def read_one_corporate(self, request):
        data = get_request_data(request)
        corporate_id = data.get('corporate_id')

        try:
            corporate = ServiceInterface().retrieve_one_record(Corporate,instance_id=corporate_id)
            queryset = corporate.values()
            print(queryset)
            data = json.dumps(list(queryset), cls=DjangoJSONEncoder)
            return JsonResponse({"code": "200.000.000", "data": data})
        except Exception as e:
            print(e)
            return JsonResponse({"code": "403.000.000", "message": "Failed"})


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
            users = ServiceInterface().retrieve_all_records(OtherUser)
            queryset = users.values()
            # print(queryset)
            data = json.dumps(list(queryset), cls=DjangoJSONEncoder)
            # data = serializers.serialize('json', [queryset])
            return data
            # json_data = json.dumps(data)
            #(OtherUser.objects.values())
            #return JsonResponse({"code": "200", "data": data})
        except Exception as e:
            print(e)
            return JsonResponse({"code": "403", "message": "failed"})

    def create_group(self, request):
        data = get_request_data(request)
        name = data.get('name')
        # permissions = data.get('permissions')
        # perm = Permission.objects.get(codename=permissions)
        # print(perm.id)

        try:

            group = ServiceInterface().create(Group, name=name)
            # group.permissions.add(permissions=perm)
            print(group.id)

            return JsonResponse({"code": "200", "message": "Success"})

        except Exception as e:
            print(e)
            return JsonResponse({"code": "403", "message": "Failed"})

    def create_permission(self, request):
        data = get_request_data(request)
        permission = data.get('permission')

        try:
            ServiceInterface().create(Permission, codename=permission)
            return JsonResponse({"code": "200", "message": "Success"})

        except Exception as e:
            print(e)
            return JsonResponse({"code": "403", "message": "Failed"})

    def attach_permission_to_group(self, request):
        data = get_request_data(request)
        name = data.get('group_name')
        permission = data.get('permission')
        print(permission)

        if not Group.objects.get(name=name):
            self.create_group(request)

        try:
            perms = []
            for codename in permission:
                perm = ServiceInterface().get(Permission,codename=codename)
                group = ServiceInterface().get(Group, name=name)
                perms.append(perm)
                # perms = [
                #     perm
                # ]
                group.permissions.set(perms)
            print(perms)
            return JsonResponse({"code": "200", "message": "Success"})

            # result = group_perm(name, permission)
            # print(result)
            # #add_post_permission = Permission.objects.get(codename=codename)
            # #group.permissions.add(add_post_permission)
            # add_employee = ServiceInterface().get(Permission, codename=result)
            # group = ServiceInterface().get(Group, name=name)
            # print(group.id)
            # print(add_employee)
            # perms = [
            #     add_employee
            # ]
            # group.permissions.set(perms)

        except Exception as e:
            print(e)
            return JsonResponse({"code": "403", "message": "Failed"})


    def authorize(self, request):
        data = get_request_data(request)
        app_name = data.get('app_name')
        # consumer_key = data.get('consumer_key')
        # consumer_secret = data.get('consumer_secret')


        try:
            consumer_key = get_random_secret_key()
            print(consumer_key)
            consumer_secret = get_random_secret_key()
            print(consumer_secret)
            token = consumer_key + ":" + consumer_secret
            base64.b64encode(token.encode()).decode()
            print(token)
            ServiceInterface().create(Authorization, app_name=app_name, consumer_key=consumer_key,
                                      consumer_secret=consumer_secret, token=token)

            return JsonResponse({"code": "200", "data": token})


        except Exception as e:
            print(e)
            return JsonResponse({"code": "403", "message": "Failed"})


