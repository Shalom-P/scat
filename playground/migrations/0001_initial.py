# Generated by Django 3.2.8 on 2021-10-23 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news_cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_sentence', models.CharField(max_length=200, verbose_name='Input Sentence')),
            ],
        ),
    ]
