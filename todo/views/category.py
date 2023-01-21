

from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from todo.models import Category
from todo.serializer import CategorySerializer, CategoryShowSerializer

@api_view(['GET', 'POST'])
def index(request):    
    if request.method == "GET":
        # Get List Data from Table categories
        categoryObj = Category.objects.all() # Get List Data
        
        categorySerializer = CategoryShowSerializer(categoryObj, many=True).data
        
        return JsonResponse({
            'category' : categorySerializer
        })
        
    elif request.method == "POST":
        # Store Data to Table categories
        body = JSONParser().parse(request)
        
        print(body)
        
        categorySerializer = CategorySerializer(data={
            'id': body['id'],
            'name': body['name']
        })
        
        # check if payload is valid
        if categorySerializer.is_valid():
            # save to database
            categorySerializer.save()
            return JsonResponse({
                'error': False,
                'message' : "Save Data Successfully"
            })
        else:
            # return error message
            return JsonResponse({
                'error': True,
                'message' : categorySerializer.errors
            })
        

@api_view(['GET', 'PUT', 'DELETE'])
def detail(request, id):
    
    # Show detail data
    if request.method == "GET":
        categoryObj = Category.objects.filter(id=id).first()
        
        categorySerializer = CategorySerializer(categoryObj).data
        
        return JsonResponse({
            'error': False,
            'data': categorySerializer
        })
        
    # Update detail data
    if request.method == "PUT":
        categoryObj = Category.objects.filter(id=id).first()
        
        body = request.data

        categorySerializer = CategorySerializer(categoryObj, data={
            'id': body['id'],
            'name': body['name']
        })
        
        if categorySerializer.is_valid():
            categorySerializer.save()
            return JsonResponse({
                'error': False,
                'data': categorySerializer.data
            })
        else:
            return JsonResponse({
                'error': True,
                'message': categorySerializer.errors
            })
            
    #Delete data
    if request.method == "DELETE":
        
        categoryObj = Category.objects.filter(id=id).first() # Hanya 1 Data
        categoryObj.delete()
        
        return JsonResponse({
            'error': False,
            'message': "Data successfully deleted"
        })
    
        