# Generated by Django 3.2.2 on 2021-11-05 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0010_auto_20211105_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos_importacao',
            name='frete',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
        migrations.AlterField(
            model_name='produtos_importacao',
            name='preco',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
        migrations.AlterField(
            model_name='produtos_loja',
            name='preco',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
    ]
