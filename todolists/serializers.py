from rest_framework import serializers
from todolists.models import  TODOList, Task, Comment

# Serializers Classes for read operations
class CommentReadSerializer (serializers.ModelSerializer):
	
	class Meta:
		model = Comment
		fields = ('text',)


class TaskReadSerializer (serializers.ModelSerializer):
	comments = CommentReadSerializer(many=True, read_only=True)
	
	class Meta:
		model = Task
		fields = ('description', 'deadline', 'done', 'order_list', 'comments')
	

class TODOListReadSerializer (serializers.ModelSerializer):
	tasks = TaskReadSerializer(many=True, read_only=True)
	
	class Meta:
		model = TODOList
		fields = ('title', 'tasks')
		

# Serializers Classes for write operations
class CommentWriteSerializer (serializers.ModelSerializer):
	
	class Meta:
		model = Comment
		fields = ('task', 'text')
		
		
class TaskWriteSerializer (serializers.ModelSerializer):
	
	class Meta:
		model = Task
		fields = ('todolist','description', 'deadline', 'done', 'order_list')
		

class TODOListWriteSerializer (serializers.ModelSerializer):
	
	class Meta:
		model = TODOList
		fields = ('title',)