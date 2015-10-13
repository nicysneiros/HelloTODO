from django.db import models

# Create your models here.
class TODOList(models.Model):
	title = models.CharField(max_length=100)
	
	def __str__ (self):
		return self.title
		
	
class Task (models.Model):
	todo_list_ref = models.ForeignKey(TODOList)
	description = models.CharField(max_length=500)
	deadline = models.DateTimeField()
	done = models.BooleanField(default=False)
	order_list = models.IntegerField()
	
	def __str__ (self):
		return self.description
		
	
class Comment (models.Model):
	task_ref = models.ForeignKey(Task)
	text = models.CharField(max_length=500)
	
	def __str__ (self):
		return self.text