# Generated by Django 3.1.1 on 2020-09-19 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0007_auto_20200919_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='meals',
        ),
        migrations.RemoveField(
            model_name='category',
            name='products',
        ),
        migrations.AddField(
            model_name='meal',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='MealCategory', to='repository.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ProductCategory', to='repository.category'),
        ),
    ]
