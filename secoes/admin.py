from django.contrib import admin
from secoes.models import Session

# Register your models here.
class Sessions(admin.ModelAdmin):
    list_display = ('user_id', 'token',)
    list_display_links = ('user_id',)
    search_fields = ('user_id',)

admin.site.register(Session, Sessions)