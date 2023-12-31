# Generated by Django 4.2.4 on 2023-09-05 04:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Adverts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Текст объявления')),
                ('photo', models.CharField(max_length=100, verbose_name='Изображение')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('category', models.SmallIntegerField(verbose_name='Категория товара')),
                ('phone_number', models.CharField(max_length=15, verbose_name='Номер телефона')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено: ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано: ')),
                ('auction', models.BooleanField(help_text='Отметьте, если торг уместен', verbose_name='Торг')),
                ('isActual', models.BooleanField(verbose_name='Акутально')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
    ]
