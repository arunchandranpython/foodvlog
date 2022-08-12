from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import prod, categ


def home(request,c_slug=None):
    c_page=None
    prodt=None
    if c_page!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        prodt=prod.objects.filter(category=c_page,available=True)
    else:
        prodt=prod.objects.all().filter(available=True)

    paginator=Paginator(prod,4)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    # try:
    #     pros=paginator.page(page)
    # except(EmptyPage,InvalidPage):
        # pros=paginator.page(paginator.num_pages)
    return render(request,'home.html',{'prodt':prodt})

def login(request):
    return render(request,'login.html')

def registration(request):
    return render(request,'registration.html')

def details(request,pro_id):
    itm=prod.objects.get(id=pro_id)
    return render(request,'item.html',{'itm':itm})

def allpro(request):
    allpro=prod.objects.all()
    return render(request,'allproducts.html',{'allpro':allpro})

def searching(request):
    pro=None
    query=None
    if 's' in request.GET:
        query=request.GET.get('s')
        pro=prod.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
        # pro = prod.objects.all()
    return render(request,"search.html",{'qr':query,'prodt':pro})

