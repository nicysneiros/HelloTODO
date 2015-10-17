from django.shortcuts import render
from todolists.models import TODOList, Task, Comment
from todolists.serializers import TODOListSerializer, TaskSerializer, CommentSerializer
from rest_framework import generics


# Create your views here.

class TODOListList (generics.ListCreateAPIView):
	queryset = TODOList.objects.all()
	serializer_class = TODOListSerializer
	
	
class TODOListDetail (generics.RetrieveUpdateDestroyAPIView):
	queryset = TODOList.objects.all()
	serializer_class = TODOListSerializer
	
	
class TaskList (generics.ListCreateAPIView):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer
	
	
class TaskDetail (generics.RetrieveUpdateDestroyAPIView):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer
	
	
class CommentList (generics.ListCreateAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	
	
class CommentDetail (generics.RetrieveUpdateDestroyAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer