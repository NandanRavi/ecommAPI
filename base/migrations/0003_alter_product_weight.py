# Generated by Django 5.1.2 on 2024-10-15 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_customer_options_alter_customer_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
