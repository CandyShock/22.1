# Generated by Django 4.2.2 on 2023-07-07 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateTimeField(verbose_name='дата'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_modified_date',
            field=models.DateTimeField(verbose_name='дата последнего изменения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='nomination',
            field=models.CharField(max_length=30, verbose_name='наименование'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(verbose_name='цена'),
        ),
    ]