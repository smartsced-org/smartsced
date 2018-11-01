from django.contrib import admin
from .models import User
class UserAdmin(admin.ModelAdmin):

    list_display = ('group', 'test', 'email','password')

admin.site.register(User, UserAdmin)
