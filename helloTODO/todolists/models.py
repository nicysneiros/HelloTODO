from django.db import models

# Create your models here.
class TODOList(models.Model):
	user = models.ForeignKey('auth.User', related_name="todolists")
	title = models.CharField(max_length=100)
	
	def __str__ (self):
		return self.title
		
	
class Task (models.Model):
	todolist = models.ForeignKey(TODOList, related_name='tasks')
	description = models.CharField(max_length=500)
	deadline = models.DateTimeField(null=True)
	done = models.BooleanField(default=False)
	order_list = models.IntegerField()
	
	def __str__ (self):
		return self.description
		
	
class Comment (models.Model):
	task = models.ForeignKey(Task, related_name='comments')
	text = models.CharField(max_length=500)
	
	def __str__ (self):
		return self.text