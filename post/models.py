from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=200) 										
	date_created = models.DateTimeField('date created')
	date_updated = models.DateTimeField('date updated')
	content = models.CharField(max_length=200)
	is_active = models.BooleanField(default=True)			

	def __str__(self):
		return 'Post: {}'.format(self.title)


class Comment(models.Model): 	
	date_created = models.DateTimeField('date created')																
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name = 'posts', null=True, blank=True) 										
