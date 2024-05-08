from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .filters import *
# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def shop(request):
    products = Product.objects.all()
    myFilter = OrderFilter(request.GET, queryset=products)
    # p = Paginator(products, 9)
    # page = request.GET.get('page')
    # prdcts = p.get_page(page)
    filtered_products = myFilter.qs
    products_count = filtered_products.count()
    context = {
        'products': filtered_products,
        'products_count': products_count,
        # 'prdcts': prdcts,
        'myFilter': myFilter,
    }
    return render(request, 'main/shop.html', context)


def product(request, id):
    details = Product.objects.get(id=id)
    related = Product.objects.filter(category=details.category)
    context = {
        'details': details,
        'related': related
    }
    return render(request, 'main/product-details.html', context)


def about(request):
    return render(request, 'main/about-us.html')


def contact(request):
    return render(request, 'main/contact-us.html')


def wishlist(request):
    return render(request, 'main/wishlist.html')


def cart(request):
    return render(request, 'main/cart.html')


def profile(request):
    user = request.user
    context = {
        'user' : user
    }
    return render(request, 'main/my-account.html',context)


def party_rooms(request):
    salles  = Salle.objects.all()
    cap99 = salles.filter(nb_place__lt=100)
    cap100200 = salles.filter(nb_place__range=[100, 199])
    cap200300 = salles.filter(nb_place__range=[200, 299])
    cap400 = salles.filter(nb_place__gte=300)
    
    print(f"""
          cap99 : {cap99}
          cap100200 : {cap100200}
          cap200300 : {cap200300}
          cap400 : {cap400}
          salles : {salles}
          """)

    context = {
        'salles' : salles,
        'cap99' : cap99,
        'cap100200' : cap100200,
        'cap200300': cap200300,
        'cap400' : cap400
    
    }
    return render(request, 'main/salle_fetes.html',context)


def room_details(request, id):
    details = Salle.objects.get(id=id)
    related = Product.objects.filter(category=details.category)
    print('_____________________________________________')
    print(details.Exta.all())
    context = {
        "details": details,
        "related": related
    }
    return render(request, 'main/sall_details.html', context)


def makeup(request):
    return render(request, 'main/contact-us.html')


def cake(request):
    return render(request, 'main/contact-us.html')


def cameraPage(request):
    teams = CameraTeam.objects.all()[:3]
    services = ExtraService.objects.all()[:10]
    context = {
        'teams': teams,
        'services': services,
    }
    return render(request, 'main/photography.html', context)
