# Generated by Django 3.2.14 on 2022-07-17 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='productdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField(null=True)),
                ('description', models.TextField()),
                ('path', models.TextField()),
            ],
        ),
    ]