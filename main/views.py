from django.shortcuts import render,get_object_or_404
from .models import *
import datetime
import markdown2
import random
# Create your views here.


def index(request):
    news = New.objects.filter(type='News').order_by('-date_post')
    most = New.objects.filter(most_popular =True).order_by('-date_post')
    trend = New.objects.filter(trending =True).order_by('-date_post')
    date_now  = datetime.datetime.now()
    main = New.objects.get(main=True)

    context={
        'news':news,
        'most':most,
        'trend':trend,
        'D_N':date_now.date(),
        'mostrend':random.choice(trend),
        'main':main
    }
    return render(request,'main/index.html',context)


def blogs(request):
    blogs = New.objects.filter(type='Blogs').order_by('-date_post')
    most = New.objects.filter(most_popular =True).order_by('-date_post')
    trend = New.objects.filter(trending =True).order_by('-date_post')
    date_now  = datetime.datetime.now()

    context={
        'blog':blogs,
        'most':most,
        'trend':trend,
        'D_N':date_now.date(),
        'mostrend':random.choice(trend)


    }
    return render(request,'main/blog.html',context)

def convert(f):

        html= markdown2.markdown(f)
        return html
def page(request,title):
    blogs = get_object_or_404(New,title=title)
    most = New.objects.filter(most_popular =True).order_by('-date_post')
    trend = New.objects.filter(trending =True).order_by('-date_post')
    print(trend)
    des = blogs.long_decsription
    des2 = convert(des)
    date_now  = datetime.datetime.now()


    context = {
        'blogs':blogs,
        'des':des2,
        'D_N':date_now.date(),
        'most':most,
        'trend':trend,
        'mostrend':random.choice(trend)


    }
    return render(request,'main/page.html',context)

def section(request,cate):
    news = New.objects.filter(cate=cate).order_by('-date_post')
    most = New.objects.filter(most_popular =True).order_by('-date_post')
    trend = New.objects.filter(trending =True).order_by('-date_post')
    date_now  = datetime.datetime.now()


    return render(request,'main/section.html',{
        'f':cate,
        'blog':news,
        'most':most,
        'D_N':date_now.date(),
        'mostrend':random.choice(trend)


    })

def privacy(request):

    most = New.objects.filter(most_popular =True).order_by('-date_post')
    trend = New.objects.filter(trending =True).order_by('-date_post')
    date_now  = datetime.datetime.now()

    return render(request,'main/privacy.html',{
        'mostrend':random.choice(trend),
        'most':most,
        'D_N':date_now.date()



    })
    
    
def about(request):

    most = New.objects.filter(most_popular =True).order_by('-date_post')
    trend = New.objects.filter(trending =True).order_by('-date_post')
    date_now  = datetime.datetime.now()

    return render(request,'main/about.html',{
        'mostrend':random.choice(trend),
        'most':most,
        'D_N':date_now.date()



    })        