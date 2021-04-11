from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WgUser
from .serializers import WgUserSerializer


class WgUserList(APIView):

    def get(self, request):
        wgusers = WgUser.objects.all()
        serializer = WgUserSerializer(wgusers, many=True)
        return Response(serializer.data)
