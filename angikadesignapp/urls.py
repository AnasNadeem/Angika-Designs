from django.urls import path
from angikadesignapp.views import (
    home,
    privacy,
    term_cond,
    about,
    products_cat,
    products_desc,
    search_result,
    min_to_max,
    max_to_min,
    min_range_max
)
urlpatterns = [
    path('', home, name='home'),
    path('category/<str:slug>/', products_cat, name='categories'),
    path('product/<str:slug>/', products_desc, name='product'),
    path('privacy_policy/', privacy, name='privacy'),
    path('terms_conditions/', term_cond, name='terms'),
    path('about/', about, name='about'),
    path('search_result/', search_result, name='search'),
    path('min_to_max/', min_to_max, name='minmax'),
    path('max_to_min/', max_to_min, name='maxmin'),
    path('min_range_max/', min_range_max, name='minrangemax'),
]