from django.shortcuts import render
from todolists.models import TODOList, Task, Comment
from todolists.serializers import TODOListWriteSerializer, TODOListReadSerializer, TaskWriteSerializer, TaskReadSerializer, CommentWriteSerializer, CommentReadSerializer
from rest_framework import generics


# Create your views here.

class TODOListList (generics.ListCreateAPIView):
	queryset = TODOList.objects.all()
	serializer_class = TODOListReadSerializer
	
	
class TODOListDetail (generics.RetrieveUpdateDestroyAPIView):
	queryset = TODOList.objects.all()
	serializer_class = TODOListWriteSerializer
	
	
class TaskList (generics.ListCreateAPIView):
	queryset = Task.objects.all()
	serializer_class = TaskReadSerializer
	
	
class TaskDetail (generics.RetrieveUpdateDestroyAPIView):
	queryset = Task.objects.all()
	serializer_class = TaskWriteSerializer
	
	
class CommentList (generics.ListCreateAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentReadSerializer
	
	
class CommentDetail (generics.RetrieveUpdateDestroyAPIView):
	queryset = Comment.objects.all()
	serializer_class = CommentWriteSerializer