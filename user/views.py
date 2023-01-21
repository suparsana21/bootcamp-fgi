from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password

from user.models import User
from user.serializers import UserSerializer
# Create your views here.

class UserList(APIView):
    
    def get(self, request):
        userObj = User.objects.all()
        
        userSerializer = UserSerializer(userObj, many= True)
        
        return JsonResponse({
            "error": False,
            "data": userSerializer.data
        })
        
    def post(self, request):
        
        payload = request.data
        
        userSerializer = UserSerializer(
            data=  {
                "username": payload['username'],
                "name": payload['name'],
                "password": make_password(password=payload['password'])
            }
        )
        
        if userSerializer.is_valid():
            userSerializer.save()
            
            return JsonResponse({
                "error": False,
                "data": userSerializer.data
            })
            
        else:
            return JsonResponse({
                "error": True,
                "data": None,
                "messages": userSerializer.errors
            })
        