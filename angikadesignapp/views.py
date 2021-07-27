from django.shortcuts import render, redirect
from angikadesignapp.models import (
    About_Angika,
    Founder_Profile,
    Categories,
    Products,
    Privacy_Policy,
    Terms_Conditions,
    Angika_Link,
    Carousel,
    MetaTags,
    MainCategories
)
from django.contrib import messages
import random
from django.db.models import Max
# Create your views here.
def home(request):
    meta_tag = MetaTags.objects.all()
    social_link = Angika_Link.objects.all()
    main_cat = MainCategories.objects.all()
    cat = Categories.objects.all()
    new_list_with_two_item = []
    list_cat = [ i for i in cat ]

    if len(list_cat)>1:
        random.shuffle(list_cat)
        for i in range(2):
            new_list_with_two_item.append(list_cat[i])
    carousel_image= Carousel.objects.all()
    context = {
        'social':social_link,
        'cat':cat,
        'cat_photo':new_list_with_two_item,
        'carousel':carousel_image,
        'main_cat':main_cat,
        'tag':meta_tag
    }
    return render(request, 'index.html', context)

def products_cat(request, slug):
    meta_tag = MetaTags.objects.all()
    cat = Categories.objects.all()
    cat_pr = Categories.objects.get(slug=slug)
    product = Products.objects.filter(category=cat_pr)
    social_link = Angika_Link.objects.all()
    main_cat = MainCategories.objects.all()
    context = {
        'social':social_link,
        'cat':cat,
        'cat_title':cat_pr,
        'prod':product,
        'tag':meta_tag,
        'main_cat':main_cat,
    }
    return render(request, 'products.html', context)

def products_desc(request, slug):
    meta_tag = MetaTags.objects.all()
    cat = Categories.objects.all()
    product_sl = Products.objects.get(slug=slug)
    social_link = Angika_Link.objects.all()
    main_cat = MainCategories.objects.all()
    context = {
        'social':social_link,
        'cat':cat,
        'prod':product_sl,
        'tag':meta_tag,
        'main_cat':main_cat,
    }
    return render(request, 'productdes.html', context)

def about(request):
    meta_tag = MetaTags.objects.all()
    cat = Categories.objects.all()
    main_cat = MainCategories.objects.all()
    ab_angika = About_Angika.objects.all()
    founder_prof = Founder_Profile.objects.all()
    social_link = Angika_Link.objects.all()
    context = {
        'about':ab_angika,
        'founder':founder_prof,
        'social':social_link,
        'cat':cat,
        'tag':meta_tag,
        'main_cat':main_cat,
    }
    return render(request, 'about.html', context)

def privacy(request):
    meta_tag = MetaTags.objects.all()
    cat = Categories.objects.all()
    main_cat = MainCategories.objects.all()
    pr_po = Privacy_Policy.objects.all()
    social_link = Angika_Link.objects.all()
    context = {
        'privacy':pr_po,
        'social':social_link,
        'cat':cat,
        'tag':meta_tag,
        'main_cat':main_cat,
    }
    return render(request, 'privacy.html', context)
    

def term_cond(request):
    meta_tag = MetaTags.objects.all()
    cat = Categories.objects.all()
    main_cat = MainCategories.objects.all()
    tm_co = Terms_Conditions.objects.all()
    social_link = Angika_Link.objects.all()
    context = {
        'terms':tm_co,
        'social':social_link,
        'cat':cat,
        'tag':meta_tag,
        'main_cat':main_cat,
    }
    return render(request, 'tc.html', context)

def searchMatch(query, item):
    if query.lower() in item.title.lower() or query.lower() in item.category.title.lower() or query.lower() in item.description.lower():
        return True
    return False

def search_result(request):
    meta_tag = MetaTags.objects.all()
    cat = Categories.objects.all()
    main_cat = MainCategories.objects.all()
    social_link = Angika_Link.objects.all()
    query = request.GET.get('search')
    if query!="" and query is not None:
        all_items = Products.objects.all()
        prod = [item for item in all_items if searchMatch(query, item)]
        context = {
            'query':query,
            'prod':prod,
            'social':social_link,
            'cat':cat,
            'tag':meta_tag,
        'main_cat':main_cat,
        }
        return render(request, 'searchres.html', context)
    else:
        messages.info(request, f"Sorry No Results.Try again with related query.")
    context = {
        'query':query,
        'social':social_link,
        'cat':cat,
        'tag':meta_tag,
        'main_cat':main_cat,
        }
    return render(request, 'searchres.html', context)


def min_to_max(request):
    meta_tag = MetaTags.objects.all()
    cat = Categories.objects.all()
    main_cat = MainCategories.objects.all()
    social_link = Angika_Link.objects.all()
    query = request.GET['search'].lower()
    all_items = Products.objects.filter(title__contains=query).order_by('main_price')
    context = {
        'prod':all_items,
        'query':query,
        'social':social_link,
        'cat':cat,
        'tag':meta_tag,
        'main_cat':main_cat,
    }
    return render(request, 'searchres.html', context)

def max_to_min(request):
    meta_tag = MetaTags.objects.all()
    cat = Categories.objects.all()
    main_cat = MainCategories.objects.all()
    social_link = Angika_Link.objects.all()
    query = request.GET['search'].lower()
    all_items = Products.objects.filter(title__contains=query).order_by('-main_price')
    context = {
        'prod':all_items,
        'query':query,
        'social':social_link,
        'cat':cat,
        'tag':meta_tag,
        'main_cat':main_cat,
    }
    return render(request, 'searchres.html', context)

def min_range_max(request):
    meta_tag = MetaTags.objects.all()
    cat = Categories.objects.all()
    main_cat = MainCategories.objects.all()
    social_link = Angika_Link.objects.all()
    query = request.GET['search'].lower()
    min_price = request.GET['min_price']
    max_price = request.GET['max_price']
    if min_price=="":
        min_price = 0
    if max_price=="":
        max_price=Products.objects.filter(title__contains=query).aggregate(Max('main_price'))['main_price__max']
    all_items = Products.objects.filter(title__contains=query,main_price__range=(min_price, max_price))
    context = {
        'prod':all_items,
        'social':social_link,
        'query':query,
        'cat':cat,
        'tag':meta_tag,
        'main_cat':main_cat,
    }
    return render(request, 'searchres.html', context)
    