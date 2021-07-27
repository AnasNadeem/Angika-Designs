from django.contrib import admin
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
# Register your models here.
admin.site.register(About_Angika)
admin.site.register(Angika_Link)
admin.site.register(Founder_Profile)
admin.site.register(Carousel)
admin.site.register(Categories)
admin.site.register(MainCategories)
admin.site.register(MetaTags)
admin.site.register(Products)
admin.site.register(Privacy_Policy)
admin.site.register(Terms_Conditions)
