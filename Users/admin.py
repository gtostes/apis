from django.contrib import admin
from Users.models import User

class Users(admin.ModelAdmin):
    list_display = ('name', 'password', 'wallet_id')
    list_display_links = ('wallet_id', 'name')
    search_fields = ('name',)

admin.site.register(User, Users)