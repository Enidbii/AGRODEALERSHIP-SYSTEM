from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from usermanage.backend.utils import get_request_data, missing_required_fields
from usermanage.backend.servicebase import ServiceInterface
from usermanage.models import OtherUser, Corporate, State



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
        required_fields = ['first_name', 'last_name', 'email', 'username', 'password', 'phone_number']

        if missing_required_fields(data, required_fields):
            return {"code": "404.000", "message": "You are missing some required fields"}
        else:
            try:
                user = User.objects.create(first_name=first_name, last_name=last_name, email=email,
                                  username=username, phone_number=phone_number)
                User.objects.get(username=username) # Retrieve a specific record
                User.objects.all() # All objects
                book = ServiceInterface().create(model=Book, name="Longhorn")
                User.objects.filter(first_name="ENID") # Filter by specific attributes
                user = ServiceInterface().create(User, first_name=first_name, last_name=last_name, email=email,
                                  username=username, phone_number=phone_number)
                user.set_password(password)
                # user.save()
                print(user.id)
                return JsonResponse({"code": "200.000", "message": "User successfully created"})
            except Exception as e:
                print(e)
                return {"code": "404.000.000", "message": "User already exists"}



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
        print(name, description, alias)

        required_fields = ['name', 'description', 'Alias']

        if missing_required_fields(data, required_fields):
            return JsonResponse({"code": "404.000", "message": "Missing the required fields"})

        try:
            corporate = ServiceInterface().create_user(Corporate, name=name, description=description, alias=alias)
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
            state = ServiceInterface().create_user(State, name=name, description=description)
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
        name = data.get("name")
        description = data.get("description")
        if not Corporate.id:
            return JsonResponse({"code": "202.000.000", "message": "The user_id does not exist"})
        try:
            corporate = Corporate.objects.get(name=name)
            print(corporate.id)
            updated = ServiceInterface().update(Corporate, instance_id=corporate.id, name=name, description=description)
            updated.save()
            return JsonResponse({"code": "200.000.000", "message": "Updated successfully"})
        except Exception as e:
            print(e)
            return JsonResponse({"code": "404.000.000", "message": "Could not be updated successfully"})







