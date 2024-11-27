from django.contrib import admin
from django.contrib.auth.models import User, Permission

from .models import OtherUser, Corporate, State, Authorization

# Register your models here.
# admin.site.unregister(User)
@admin.register(OtherUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'username', 'created_at', 'updated_at', 'is_superuser', 'is_active', 'is_staff', 'status']
    list_filter = ('status', 'created_at', 'updated_at')
    search_fields = ['first_name', 'last_name', 'username', 'email']
    readonly_fields = ('created_at', 'updated_at', 'last_login')
# admin.site.register(OtherUser)
admin.site.register(Corporate)
admin.site.register(State)
admin.site.register(Permission)
admin.site.register(Authorization)

