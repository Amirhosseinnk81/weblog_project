from django.shortcuts import render
from post_app.models import article

def home(request):
    articles = article.objects.all()
    return render(request , "home_app/index.html" , {'articles':articles})