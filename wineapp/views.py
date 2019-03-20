from django.shortcuts import render
from .models import Wine
from django.shortcuts import render
from .filters import WineFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    wine_list = Wine.objects.all().order_by('price')
    page = request.GET.get('page', 1)
    paginator = Paginator(wine_list, 10)
    try:
        wines = paginator.page(page)
    except PageNotAnInteger:
        wines = paginator.page(1)
    except EmptyPage:
        wines = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'wines': wines})

def search(request):
    # Need to do some work
    wine_list = Wine.objects.all()[10]
    wine_filter = WineFilter(request.GET, queryset=wine_list)
    return render(request, 'wine_list.html', {'filter': wine_filter})


def aboutus(request):
    context = {}
    return render(request, 'aboutus.html', context)

def contactus(request):
    context = {}
    return render(request, 'contactus.html', context)
