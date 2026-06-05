from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog,Category

# Create your views here.

def posts_by_category(request,category_id):
    # fetch posts belongs to the specify category with category_id
    posts=Blog.objects.filter(status='Published',category=category_id)
    # use try except when you want user to redirect or do some custom action instead of showing error if category doesnot exist
    # try:
    #     category=Category.objects.get(pk=category_id)
    # except:
    #     return redirect('home')
     
    # use getobject_or_404 when you want to show 404 error page if the category doesnot exist
    category=get_object_or_404(Category,pk=category_id)
    context={
        'posts':posts,
        'category':category
    }
    return render(request,'posts_by_category.html',context)
