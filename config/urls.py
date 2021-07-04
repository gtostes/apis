"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Cryptocurrencies.views import CoinsViewSet
from secoes.views import SessionsViewSet
from Users.views import UsersViewSet
from wallets.views import UsersWViewSet

router = routers.DefaultRouter()
router.register(r'Cryptocurrencies', CoinsViewSet)
router.register(r'Sessions', SessionsViewSet)
router.register(r'Users', UsersViewSet)
router.register(r'Wallets', UsersWViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
