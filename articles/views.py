from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms

def article_list(request):
	articles = Article.objects.all().order_by('date')
	return render(request, 'articles/article_list.html', { 'articles': articles })

# View individual blog article
def article_detail(request, id): 
	article = Article.objects.get(id=id)
	return render(request, 'articles/article_detail.html', { 'article': article })

# Update blog article
@login_required(login_url="/accounts/login")
def article_update(request, id):
    article = Article.objects.get(id=id)
    if request.method == "POST":
        form = forms.CreateArticle(request.POST, instance=article)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle(instance=article)
    return render(request, 'articles/article_update.html', {'form': form, 'article': article})

# Add new blog article
@login_required(login_url="/accounts/login/")
def article_create(request):

	# Check to see if the form was submitted
	if request.method == 'POST':

		form = forms.CreateArticle(request.POST, request.FILES)

		# Check if the form is valid
		if form.is_valid():

			# Create save form instance but dont commit it
			instance = form.save(commit=False)

			# Add author to the form instance
			instance.author = request.user

			# Save the form submission
			instance.save()

			# Redirect user to article list
			return redirect('articles:list')
	else:

		# Build form from forms.py
		form = forms.CreateArticle()

	# Render the article creation template and pass the form to it
	return render(request, 'articles/article_create.html', { 'form':form })


# Delete blog post
@login_required(login_url="/accounts/login/")
def confirm_delete(request, id):

	# Grab article by the id and create new object
	article = Article.objects.get(id=id)

	# Delete object
	article.delete()

	# Return user to articles list page
	return redirect('articles:list')