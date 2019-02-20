# Generated by Django 2.1.5 on 2019-02-20 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0087_auto_20190208_0326'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description_json',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='categorytranslation',
            name='description_json',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='description_json',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='collectiontranslation',
            name='description_json',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_json',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='producttranslation',
            name='description_json',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='collection',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='producttranslation',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
