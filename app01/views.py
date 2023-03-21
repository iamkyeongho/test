from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from app01.forms import *

app_name = "app01"

def index(request):
    page = request.GET.get("page", '1')  # 페이지 정보를 받아오고 없으면 초기값 1
    blog_list = Blog.objects.order_by("-create_date") # order by create_date desc
    paginator = Paginator(blog_list, 10)  # 10개씩
    page_obj = paginator.get_page(page)
    context = {"title":"테스트", "blog_list":page_obj}
    return render(request, "app01/index.html", context)

def create_blog(request):
    if request.method == "GET":
        form = BlogForm()
        context = {"form":form}
        return render(request, "app01/create_blog.html", context)
    elif request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.save()
            return redirect("app01:index")

def modify_blog(request, id:int):
    blog = Blog.objects.get(id=id)    
    if request.method == "GET":
        form = BlogForm(instance=blog)
        context = {"form":form}
        return render(request, "app01/modify_blog.html", context)
    elif request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.save()
            return redirect("app01:index")            