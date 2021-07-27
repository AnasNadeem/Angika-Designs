# Generated by Django 3.2.5 on 2021-07-27 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_Angika',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('angika_image', models.ImageField(upload_to='angika')),
                ('history', models.TextField(blank=True)),
                ('categories', models.TextField(blank=True)),
                ('aim', models.TextField(blank=True)),
                ('award', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Angika_Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='angika')),
                ('include_this_logo_in_navbar', models.BooleanField(default=False)),
                ('angika_about_description', models.TextField()),
                ('facebook_link', models.CharField(blank=True, max_length=100)),
                ('instagram_username', models.CharField(blank=True, max_length=100)),
                ('twitter_username', models.CharField(blank=True, max_length=100)),
                ('whatsapp_number', models.CharField(blank=True, max_length=100)),
                ('linkedin_link', models.CharField(blank=True, max_length=100)),
                ('gmail', models.CharField(blank=True, max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_image', models.ImageField(upload_to='carousel')),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('portrait_image', models.ImageField(upload_to='categories')),
                ('landscape_image', models.ImageField(null=True, upload_to='categories')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Founder_Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('founder_name', models.CharField(max_length=100)),
                ('founder_quote', models.TextField()),
                ('founder_image', models.ImageField(upload_to='angika')),
                ('facebook_link', models.CharField(blank=True, max_length=100)),
                ('instagram_username', models.CharField(blank=True, max_length=100)),
                ('twitter_username', models.CharField(blank=True, max_length=100)),
                ('whatsapp_number', models.CharField(blank=True, max_length=100)),
                ('linkedin_link', models.CharField(blank=True, max_length=100)),
                ('gmail', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MainCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('for_title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MetaTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.TextField(blank=True, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Privacy_Policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('statement', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Terms_Conditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200)),
                ('statement', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('main_image', models.ImageField(upload_to='products')),
                ('second_image', models.ImageField(blank=True, null=True, upload_to='products')),
                ('third_image', models.ImageField(blank=True, null=True, upload_to='products')),
                ('main_price', models.IntegerField()),
                ('main_cut_price', models.IntegerField(blank=True, null=True)),
                ('color', models.CharField(max_length=100)),
                ('cloth_type', models.CharField(max_length=100)),
                ('customizable', models.BooleanField(default=True)),
                ('description', models.TextField()),
                ('small_size', models.BooleanField(default=False)),
                ('medium_size', models.BooleanField(default=False)),
                ('large_size', models.BooleanField(default=False)),
                ('xl_size', models.BooleanField(default=False)),
                ('xxl_size', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='angikadesignapp.categories')),
            ],
        ),
        migrations.AddField(
            model_name='categories',
            name='main_cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='angikadesignapp.maincategories'),
        ),
    ]