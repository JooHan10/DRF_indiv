from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from todos.models import ToDoList
from todos.serializers import ToDoSerializer, ToDoListSerializer, ToDoCreateSerializer
import datetime


class ToDoView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        todos = ToDoList.objects.all()
        serializer = ToDoListSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ToDoCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ToDoDetailView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    def get(self, request, todo_id):
        todos = get_object_or_404(ToDoList, id=todo_id)
        serializer = ToDoSerializer(todos)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, todo_id):
        todos = get_object_or_404(ToDoList, id=todo_id)
        if request.user == todos.user:
            serializer = ToDoCreateSerializer(todos, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이 없습니다!", status=status.HTTP_403_FORBIDDEN)
    
    def delete(self, request, todo_id):
        todos = get_object_or_404(ToDoList, id=todo_id)
        if request.user == todos.user:
            todos.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다!", status=status.HTTP_403_FORBIDDEN)


class MockView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        return Response("get 요청")


class ToDoCompleteView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    def put(self, request, todo_id):
        todos = get_object_or_404(ToDoList, id=todo_id)
        if request.user == todos.user:
            serializer = ToDoSerializer(todos, data=request.data)
            if serializer.is_valid():
                if request.data.get('is_complete') == "True":
                    serializer.save(completion_at = datetime.datetime.now())
                    return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)