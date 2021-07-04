from rest_framework import serializers
from .models import Session

class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        fields = ('user_id', 'tokens')