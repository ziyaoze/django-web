# Generated by Django 4.1.1 on 2022-09-12 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='home',
            options={'verbose_name_plural': 'Home Page'},
        ),
        migrations.AddField(
            model_name='home',
            name='navlink1_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='navlink1_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='navlink2_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='navlink2_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='navlink3_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='navlink3_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='navlink4_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='navlink4_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='navlink5_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='navlink5_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='navlink6_dropdown_item1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='navlink6_dropdown_item1_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='navlink6_dropdown_item2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='navlink6_dropdown_item2_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='home',
            name='navlink6_dropdown_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
