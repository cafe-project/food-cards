# Generated by Django 3.1.1 on 2020-09-17 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='Product', to='repository.Product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='repository.category'),
        ),
    ]