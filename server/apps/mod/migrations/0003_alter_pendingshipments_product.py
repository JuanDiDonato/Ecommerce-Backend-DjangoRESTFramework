# Generated by Django 3.2.9 on 2021-12-16 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('mod', '0002_pendingshipments_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendingshipments',
            name='product',
            field=models.ForeignKey(default='<django.db.models.query_utils.DeferredAttribute object at 0x0000028BCE5AADA0>', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='products.product'),
        ),
    ]