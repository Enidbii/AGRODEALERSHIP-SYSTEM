from django.urls import path, include

urlpatterns = [
    # path('', views.home, name="home"),
    # path('register/', views.register, name="register"),
    path("auth/", include("usermanage.backend.endpoints"))
]