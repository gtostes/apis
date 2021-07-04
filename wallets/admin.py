from django.contrib import admin
from wallets.models import User

class Users(admin.ModelAdmin):
    list_display = ('user_id', 'amount', 'crypto_amounts')
    list_display_links = ('user_id',)
    search_fields = ('user_id',)

admin.site.register(User, Users)