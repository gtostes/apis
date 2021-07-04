# Register your models here.
from django.contrib import admin
from Cryptocurrencies.models import Coin
from Users.models import User

class Coins(admin.ModelAdmin):
    list_display = ('name', 'today_rate_usd', 'historical_data_30day')
    list_display_links = ('name',)
    search_fields = ('name',)

admin.site.register(Coin, Coins)