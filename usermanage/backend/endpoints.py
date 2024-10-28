"""
Endpoints
"""
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .authentication import AuthenticateUser

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

def delete_user(request):
    try:
        return JsonResponse(AuthenticateUser().delete(request), safe=False)
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def update(request, user_id):
    try:
        return HttpResponse(AuthenticateUser().update(request, user_id))
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

from django.urls import path

urlpatterns = [
    path('login/', login, name="login"),
    path('register/', create_user, name="create" ),
    path('update/<int:user_id>/', update, name="update"),
    path('logout/', logout, name="logout"),
    path('create_corporate/', create_corporate, name="create_corporate")
]