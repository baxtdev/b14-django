from django.shortcuts import render

# Create your views here.
def main_page(request):
    user_data = {
        'name':'John',
        'age':28,
        'is_merried':False
    }
    return render(request=request,template_name='news/index.html',context=user_data)