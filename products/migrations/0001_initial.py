# Generated by Django 3.2.11 on 2022-01-12 19:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('url', models.URLField(blank=True, null=True)),
                ('price', models.PositiveIntegerField()),
                ('refund', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('platform', models.CharField(choices=[('amazon', 'Amazon'), ('flipkart', 'Flipkart'), ('meesho', 'Meesho'), ('other', 'Other')], max_length=64)),
                ('review_type', models.CharField(choices=[('review', 'Review'), ('rating', 'Rating'), ('seller_feedback', 'Seller Feedback'), ('social_media', 'Social Media'), ('other', 'Other')], max_length=64)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('mediator_only', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
