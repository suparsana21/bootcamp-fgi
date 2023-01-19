from django.http import HttpResponse, JsonResponse
from rest_framework.views import APIView

from todo.models import Category
from todo.serializer import CategorySerializer


class CategoryList(APIView):
    
    def get(self, request, format=None):
        
        categoryObj = Category.objects.all()
        
        categorySerializer = CategorySerializer(categoryObj, many=True)
        
        return JsonResponse({
            'error': False,
            'data': categorySerializer.data
        })
        

