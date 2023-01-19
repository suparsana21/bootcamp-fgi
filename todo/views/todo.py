
from django.http import JsonResponse
from rest_framework.views import APIView
from todo.models import Todo

from todo.serializer import TodoSerializer, TodoShowSerializer

class TodoList(APIView):
    
    def get(self, request):
        
        todoObj = Todo.objects
        
        if request.GET.get('category_id') is not None and request.GET.get('category_id') != "":
            todoObj = todoObj.filter( category = request.GET.get('category_id'))
        
        if request.GET.get('category_name') is not None and request.GET.get('category_name') != "":
            todoObj = todoObj.filter(category__name__contains=request.GET.get('category_name'))
        x         
        
        # Conditional field gt (greater than), gte (greater than equals), lt (less than), lte (less than equals)
        
        # Filter
        # Class.objects.filter(column_name=keyword)
        # Class.objects.filter(column_name__contains=keyword) // Seperti query LIKE %% pada SQL
        # Class.objects.filter(relation_field__relational_field_name=keyword)
        # Class.objects.filter(relation_field__in=array)
        
        # Mahasiswa.objects.filter(name__contains='ALEX')
        # Mahasiswa.objects.filter(jurusan='SI')
        # Mahasiswa.objects.filter(nim__in=('001','002','003'))
        
        todoSerializer = TodoShowSerializer(todoObj, many=True)
        
        return JsonResponse({
            "error": False,
            "data": todoSerializer.data,
            "message": "Get data successfully"
        })
        
        
    def post(self, request):
        
        body = request.data 
        
        todoSerializer = TodoSerializer(data={
            "name": body['name'],
            "category": body['category_id']
        })
        
        if todoSerializer.is_valid():
            todoSerializer.save()
            
            return JsonResponse({
              "error": False,
              "data": todoSerializer.data,
              "message": "Data saved successfully"
            })
            
        else:
            
            return JsonResponse({
                "error": True,
                "data": None,
                "message": todoSerializer.errors
            })


class TodoDetail(APIView):
    
    def get(self, request, id):
        
        todoObj = Todo.objects.filter(id=id).first()
        
        todoSerializer = TodoShowSerializer(todoObj)
        
        return JsonResponse({
            "error": False,
            "data": todoSerializer.data
        })
        
    def put(self, request, id):
        
        body = request.data 
        
        todoObj = Todo.objects.filter(id=id).first()
        
        todoSerializer = TodoSerializer(todoObj, data={
            "name": body['name'],
            "category": body['category_id']
        })
        
        if todoSerializer.is_valid():
            todoSerializer.save()
            
            return JsonResponse({
                "error": False,
                "data": todoSerializer.data,
                "message": "Data updated successfully"
            })
        
        else :
            return JsonResponse({
                "data": None,
                "error": True,
                "message": todoSerializer.errors
            })
            
    def delete(self, request, id):
        
        todoObject = Todo.objects.filter(id=id)
        
        todoObject.delete()
        
        return JsonResponse({
            "error": False,
            "data": None,
            "message": "Data deleted successfully"
        })