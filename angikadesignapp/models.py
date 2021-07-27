from django.db import models

# Create your models here.

class MainCategories(models.Model):
    for_title = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.for_title}'

class Categories(models.Model):
    main_cat = models.ForeignKey(MainCategories, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100)
    portrait_image = models.ImageField(upload_to="categories")
    landscape_image = models.ImageField(upload_to="categories", null=True)
    mention_with_pink_bg = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        self.slug = f'{self.title}'
        super().save(*args, **kwargs)

class Products(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    main_image = models.ImageField(upload_to='products')
    second_image = models.ImageField(upload_to='products', null=True, blank=True)
    third_image = models.ImageField(upload_to='products', null=True, blank=True)
    main_price = models.IntegerField()
    main_cut_price = models.IntegerField(null=True,blank=True)
    color = models.CharField(max_length=100)
    cloth_type = models.CharField(max_length=100)
    customizable = models.BooleanField(default=True)
    description = models.TextField()
    small_size = models.BooleanField(default=False)
    medium_size = models.BooleanField(default=False)
    large_size = models.BooleanField(default=False)
    xl_size = models.BooleanField(default=False)
    xxl_size = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return f'{self.title}: {self.category}'

    def save(self, *args, **kwargs):
        self.slug = f'{self.title}_{self.category.title}'
        super().save(*args, **kwargs)

class Carousel(models.Model):
    c_image = models.ImageField(upload_to="carousel")
    def __str__(self):
        return 'Carousel Image'

class About_Angika(models.Model):
    angika_image = models.ImageField(upload_to='angika')
    history = models.TextField(blank=True)
    categories = models.TextField(blank=True)
    aim = models.TextField(blank=True)
    award = models.TextField(blank=True)

    def __str__(self):
        return 'About Angika'

class Founder_Profile(models.Model):
    founder_name = models.CharField(max_length=100)
    founder_quote = models.TextField()
    founder_image = models.ImageField(upload_to='angika')
    facebook_link = models.CharField(max_length=100, blank=True)
    instagram_username = models.CharField(max_length=100, blank=True)
    twitter_username = models.CharField(max_length=100, blank=True)
    whatsapp_number = models.CharField(max_length=100, blank=True)
    linkedin_link = models.CharField(max_length=100, blank=True)
    gmail = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.founder_name}: {self.founder_quote}'

class Angika_Link(models.Model):
    logo = models.ImageField(upload_to="angika",null=True, blank=True)
    include_this_logo_in_navbar = models.BooleanField(default=False)
    angika_about_description = models.TextField()
    facebook_link = models.CharField(max_length=100, blank=True)
    instagram_username = models.CharField(max_length=100, blank=True)
    twitter_username = models.CharField(max_length=100, blank=True)
    whatsapp_number = models.CharField(max_length=100, blank=True)
    linkedin_link = models.CharField(max_length=100, blank=True)
    gmail = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f'{self.instagram_username} {self.phone_number}'

class Privacy_Policy(models.Model):
    title = models.CharField(max_length=200, blank=True)
    statement = models.TextField()

    def __str__(self):
        return f'{self.title} - {self.statement}'

class Terms_Conditions(models.Model):
    title = models.CharField(max_length=200, blank=True)
    statement = models.TextField()

    def __str__(self):
        return f'{self.title} - {self.statement}'

class MetaTags(models.Model):
    keyword = models.TextField(null=True, blank=True)
    desc = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Keywords: {self.keyword}"