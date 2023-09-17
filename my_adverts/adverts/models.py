from django.db import models
from django.utils import timezone
from django.utils.html import format_html
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.utils.safestring import mark_safe


# Create your models here.
# Adverts -- класс объявлений
# title -- заголовок
# content -- текст объявлений
# photo -- фото объявлений
# price -- цена
# category -- категория товара
# phone_number -- номер телефона
# updated_at -- дата обновления
# created_at -- дата создания
# auction -- уместен ли торг
# isSctual -- актуально ли обновление
#
#

User = get_user_model()

class Adverts(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    content = models.TextField("Текст объявления")
    photo = models.ImageField("Изображение", upload_to='my_adverts')
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    category = models.SmallIntegerField("Категория товара")
    phone_number = models.CharField("Номер телефона", max_length=15)
    updated_at = models.DateTimeField("Обновлено: ", auto_now=True)
    created_at = models.DateTimeField("Создано: ", auto_now_add=True)
    user = models.ForeignKey(User, verbose_name ="Автор", on_delete=models.CASCADE)
    auction = models.BooleanField("Торг", help_text ="Отметьте, если торг уместен")
    isActual = models.BooleanField("Акутально")
    
    
    @admin.display(description="Дата создания")
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.strftime("%H:%M:%S")
            return format_html('<span style="color: green; font-weight: bold">Сегодня в {}</span>', created_time)
        return self.created_at.strftime("%d.%m.%Y в %H:%M:%S")
        
        
        
    @admin.display(description="Дата обновление")
    def update_date(self):
        if self.updated_at.date() == timezone.now().date():
            update_time = self.updated_at.strftime("%H:%M:%S")
            return format_html('<span style="color: green; font-weight: bold">Сегодня в {}</span>', update_time)
        return self.updated_at.strftime("%d.%m.%Y в %H:%M:%S")
     

    @admin.display(description = "картинка")
    def created_foto(self):
        if self.photo:
            return format_html(
                '<img src = "/media/{}" style = "width:100px; hight:100px;"> ',self.photo
            )
        else:
            return format_html(
                '<img src = "/static/img/adv.png" style = "width:100px; hight:100px;"> '
            )


