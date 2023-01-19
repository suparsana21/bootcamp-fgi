from rest_framework import serializers

from todo.models import Category, Todo

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = (
            'id',
            'name'
        )
        

class TodoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Todo
        fields = (
            'id',
            'name',
            'category'
        )
        

class TodoShowSerializer(serializers.ModelSerializer):
    
    category = CategorySerializer()
    
    class Meta:
        model = Todo
        fields = (
            'id',
            'name',
            'category'
        )