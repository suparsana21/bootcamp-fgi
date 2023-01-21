from rest_framework import serializers

from todo.models import Category, Todo

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = (
            'id',
            'name'
        )
        

class CategoryShowSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'todos'
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
    
    # category = CategorySerializer()
    category = serializers.StringRelatedField(source="get_category_name")
    
    class Meta:
        model = Todo
        fields = (
            'id',
            'name',
            'category'
        )