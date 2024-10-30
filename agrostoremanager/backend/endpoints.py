from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from agrostoremanager.backend.authenticate import AgroStore


@csrf_exempt
def register(request):
    try:
        return HttpResponse(AgroStore().register(request))
    except Exception as e:
        print(e)
        return None

@csrf_exempt
def login(request):
    try:
        return HttpResponse(AgroStore().login(request))
    except Exception as ex:
        print(ex)
        return None

@csrf_exempt
def update_user(request):
    try:
        return HttpResponse(AgroStore().update(request))
    except Exception as ex:
        print(ex)
        return None




from django.urls import path

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login, name="login"),
    path("update_user", update_user, name="update_user")
]