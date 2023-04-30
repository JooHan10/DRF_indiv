from rest_framework import serializers
from todos.models import ToDoList


class ToDoSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.email
    
    class Meta:
        model = ToDoList
        fields = '__all__'


class ToDoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ("title", "is_complete")


class ToDoListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    
    def get_user(self, obj):
        return obj.user.email
    
    class Meta:
        model = ToDoList
        fields = ('pk', 'title', 'user', 'is_complete', 'created_at','updated_at', 'completion_at')