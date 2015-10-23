from django.contrib import admin

# Register your models here.
'''
from .models import TODOList, Task, Comment

class CommentInline(admin.StackedInline):
	model = Comment
	extra = 1
	
	
class TaskAdmin (admin.ModelAdmin):
	inlines = [CommentInline]
	
	
class TaskInline(admin.StackedInline):
	model = Task
	extra = 1
	
	
class TODOListAdmin(admin.ModelAdmin):
	inlines = [TaskInline]
	
	
admin.site.register(TODOList, TODOListAdmin)
'''
