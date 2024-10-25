from django.contrib import admin
from django.contrib.auth.models import User

from .models import OtherUser, Corporate, State
# Register your models here.
# admin.site.unregister(User)
# @admin.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):
    # list_display = ['first_name', 'last_name', 'username', 'created_at', 'updated_at', 'is_superuser', 'is_active', 'is_staff', 'status']
    # list_filter = ('status', 'created_at', 'updated_at')
    # search_fields = ['first_name', 'last_name', 'username', 'email']
    # readonly_fields = ('created_at', 'updated_at', 'last_login')
admin.site.register(OtherUser)
admin.site.register(Corporate)
admin.site.register(State)

