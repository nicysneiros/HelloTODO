from rest_framework import serializers
from todolists.models import  TODOList, Task, Comment


class TODOListSerializer (serializers.ModelSerializer):
	
	class Meta:
		model = TODOList
		fields = ('title', 'task_set')
		

class TaskSerializer (serializers.ModelSerializer):
	
	class Meta:
		model = Task
		fields = ('description', 'deadline', 'done', 'order_list', 'comment_set')
	
		
class CommentSerializer (serializers.ModelSerializer):
	
	class Meta:
		model = Comment
		fields = ('text')