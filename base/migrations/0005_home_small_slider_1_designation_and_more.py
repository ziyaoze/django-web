# Generated by Django 4.1.1 on 2022-09-12 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_home_who_we_1_heading_home_who_we_1_img_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='small_slider_1_designation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='small_slider_1_person',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='small_slider_1_person_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/home/'),
        ),
        migrations.AddField(
            model_name='home',
            name='small_slider_1_text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='small_slider_2_designation',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='small_slider_2_person',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='small_slider_2_person_img',
            field=models.ImageField(blank=True, null=True, upload_to='images/home/'),
        ),
        migrations.AddField(
            model_name='home',
            name='small_slider_2_text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
