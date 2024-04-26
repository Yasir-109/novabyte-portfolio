# Generated by Django 5.0.4 on 2024-04-24 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('url', models.URLField()),
                ('image', models.ImageField(upload_to='portfolio/images/')),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('category', models.CharField(choices=[('Python', 'Python'), ('dot net', 'dot net'), ('SEO', 'SEO')], max_length=20)),
            ],
        ),
    ]
