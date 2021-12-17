# Generated by Django 3.2.9 on 2021-12-17 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20211217_1430'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name': 'image', 'verbose_name_plural': 'images'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AlterField(
            model_name='images',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.product'),
        ),
    ]