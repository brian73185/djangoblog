from django import forms
from . import models

# Blog post form fields
class CreatePost(forms.ModelForm):
	class Meta:
		model = models.Article
		fields = ['title', 'body', 'slug']