from rest_framework import serializers
from todolists.models import  TODOList, Task, Comment


class CommentSerializer (serializers.ModelSerializer):
	
	class Meta:
		model = Comment
		fields = ('text',)


class TaskSerializer (serializers.ModelSerializer):
	comments = CommentSerializer(many=True, read_only=True)
	
	class Meta:
		model = Task
		fields = ('description', 'deadline', 'done', 'order_list', 'comments')
	

class TODOListSerializer (serializers.ModelSerializer):
	tasks = TaskSerializer(many=True, read_only=True)
	
	class Meta:
		model = TODOList
		fields = ('title', 'tasks')
		