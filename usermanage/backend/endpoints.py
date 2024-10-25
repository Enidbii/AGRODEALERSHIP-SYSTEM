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
def update(request):
    try:
        return HttpResponse(AuthenticateUser().update(request))
    except Exception as e:
        print(e)
        return None

from django.urls import path

urlpatterns = [
    path('login/', login, name="login"),
    path('register/', create_user, name="create" ),
    path('update/', update, name="update")
]