"""
Endpoints
"""
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .authentication import AuthenticateUser
from .datatables import Querying


@csrf_exempt
def login(request):
    #try:
    return HttpResponse(AuthenticateUser().login(request))
    # except Exception as e:
    #     print(e)
    #     return None

@csrf_exempt
def create_user(request):
    try:
        return HttpResponse(AuthenticateUser().register(request))
    except Exception as e:
        print(e)
        return None
@csrf_exempt
def delete_user(request):
    try:
        return HttpResponse(AuthenticateUser().delete_user(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def update(request):
    try:
        return HttpResponse(AuthenticateUser().update(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def logout(request):
    try:
        return HttpResponse(AuthenticateUser().logout(request))
    except Exception as e:
        print(e)
        return None
@csrf_exempt
def create_corporate(request):
    try:
        return HttpResponse(AuthenticateUser().create_corporate(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def add_state(request):
    try:
        return HttpResponse(AuthenticateUser().add_state(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def delete_user(request):
    try:
        return HttpResponse(AuthenticateUser().delete_user(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def read_user(request):
    try:
        return HttpResponse(AuthenticateUser().read_user(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def corporate_update(request):
    try:
        return HttpResponse(AuthenticateUser().update_corporate(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def read_corporate(request):
    try:
        return HttpResponse(AuthenticateUser().read_corporates(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def delete_corporate(request):
    try:
        return HttpResponse(AuthenticateUser().delete_corporate(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def read_a_corporate(request):
    try:
        return  HttpResponse(AuthenticateUser().read_one_corporate(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def create_group(request):
    try:
        return HttpResponse(AuthenticateUser().create_group(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def records(request):
    try:
        return HttpResponse(AuthenticateUser().get_records())
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def create_permission(request):
    try:
        return HttpResponse(AuthenticateUser().create_permission(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def attach_permission_to_group(request):
    try:
        return HttpResponse(AuthenticateUser().attach_permission_to_group(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def auth_corp(request):
    try:
        return HttpResponse(AuthenticateUser().authorize(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def check_auth(request):
    try:
        return  HttpResponse(AuthenticateUser().check_authorization(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def query_employees(request):
    try:
        return HttpResponse(Querying().query_employees(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def active_employees(request):
    try:
        return HttpResponse(Querying().active_users(request))
    except Exception as e:
        print(e)
        return None

from django.urls import path

urlpatterns = [
    path('login/', login, name="login"),
    path('register/', create_user, name="create" ),
    path('update/', update, name="update"),
    path('read-user/', read_user, name="read_user"),
    path('logout/', logout, name="logout"),
    path('create_corporate/', create_corporate, name="create_corporate"),
    path('add_state/', add_state, name="add_state"),
    path('delete/', delete_user, name="delete"),
    path('corporate_update/', corporate_update, name="corporate_update"),
    path('read-corporates/', read_corporate, name="read_corporate"),
    path('read-one-corporate/', read_a_corporate, name="read_one_corporate"),
    path('delete-corporate/', delete_corporate, name= "delete_corporate"),
    path('create-group/', create_group, name="create_group"),
    path('retrieve-records/', records, name="records"),
    path('create-permissions/', create_permission, name= "create_permission"),
    path('attach-permission-group/', attach_permission_to_group, name="attach_permission_to_group"),
    path('auth-corp/', auth_corp, name="auth_corp"),
    path('auth-check/', check_auth, name="check_auth"),
    path("get-corporate-employees/", query_employees, name='get_employees'),
    path("active-employees/", active_employees, name='get_employees')
]