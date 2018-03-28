from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):

	# Title of the blog
	title = models.CharField(max_length=100)

	# The slugline (what the url shows) of the blog
	slug = models.SlugField()

	# The body of the blog
	body = models.TextField()

	# The date and time the article post was created (defaulted to "now")
	date = models.DateTimeField(auto_now_add=True)
	# thumb = models.ImageField(default='default.png', blank=True)

	# The author of the blog post (a foreign key from the users table)
	author = models.ForeignKey(User, default=1, on_delete=models.PROTECT)

	def __str__(self):
		return self.title

	# Take the first 50 characters of the body and add ... to it for the article list page
	def snippet(self):
		return self.body[:50] + '...'