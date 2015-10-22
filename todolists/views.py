from django.shortcuts import render
from todolists.models import TODOList, Task, Comment
from todolists.serializers import TODOListWriteSerializer, TODOListReadSerializer, TaskWriteSerializer, TaskReadSerializer, CommentWriteSerializer, CommentReadSerializer
from rest_framework import generics, permissions
from oauth2_provider.models import Application


# Create your views here.
class TODOListList (generics.ListCreateAPIView):
	permission_classes = (permissions.IsAuthenticated, )
	serializer_class = TODOListReadSerializer
	
	def get_queryset(self):
		user = self.request.user
		return TODOList.objects.filter(user=user)
	
	def perform_create(self, serializer):
		serializer.save(user=self.request.user)
	
	
class TODOListDetail (generics.RetrieveUpdateDestroyAPIView):
	serializer_class = TODOListWriteSerializer
	permission_classes = (permissions.IsAuthenticated,)
	
	def get_queryset(self):
		user = self.request.user
		return TODOList.objects.filter(user=user)

	
	
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