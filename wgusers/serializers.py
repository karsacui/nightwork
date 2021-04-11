from rest_framework import serializers
from .models import WgUser
from datetime import date


class WgUserSerializer(serializers.ModelSerializer):
    expire = serializers.SerializerMethodField('is_expired')

    def is_expired(self, wguser):
        return date.today() > wguser.expire_date

    class Meta:
        model = WgUser
        fields = ['serial_number', 'public_key', 'expire']


