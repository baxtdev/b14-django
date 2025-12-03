from django.shortcuts import render

from .models import News

# Create your views here.
def main_page(request):
    news = News.objects.all()
    context = {
        'news':news
    }
    return render(request=request,template_name='news/index.html',context=context)