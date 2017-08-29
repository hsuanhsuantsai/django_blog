from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(blank=True)
	highlight = models.TextField(blank=True)
	photo = models.ImageField(upload_to='photos/', default='photos/default.png', blank=True)
	location = models.CharField(max_length=100, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	tags = models.CharField(max_length=100, default='', blank=True)

	def __str__(self):
		return self.title
