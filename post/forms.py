from django.forms import ModelForm
from .models import Post
from .models import Comment

class PostModelForm(ModelForm):
	class Meta:
		model = Post
		exclude = ['id']
		exclude = ['is_active']


class New_Post(ModelForm):
	class Meta:
		model = Post
		exclude = ['id']
		exclude = ['is_active']


class PostCommentForm(ModelForm):
	class Meta:
		model = Comment
		exclude = ['id']


class New_Comment(ModelForm):
	class Meta:
		model = Comment
		exclude = ['id']