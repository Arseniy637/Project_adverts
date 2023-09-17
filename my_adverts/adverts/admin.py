from django.contrib import admin
from .models import Adverts
from django.utils.html import format_html
# Register your models here.

class AdvertsAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'created_date', 'update_date', 'isActual', 'auction', 'category', 'created_foto']
    liset_filter = ['isActual', 'auction', 'category']
    actions = ['make_auction_actual', 'make_auction_not_actual', 'make_advert_actual', 'make_advert_not_actual']
    fieldsets = (
        ('Общее', {
            'fields' : ('title', 'content', 'category', 'user', 'photo'),
            'classes' : ['collapse']
        }),
        ('Финансы', {
            'fields' : ('price', 'auction', 'isActual'),
            'classes' : ['collapse']
         })
    )
    
    

    
    
    @admin.action(description="Actualize the auction")
    def make_auction_actual(self, request, queryset):
        queryset.update(auction=True)
        
    @admin.action(description='Deactualize the auction')
    def make_auction_not_actual(self, request, queryset):
        queryset.update(auction=False)
        
    @admin.action(description='Actualize the advert')
    def make_advert_actual(self, request, queryset):
        queryset.update(isActual=True)
        
    @admin.action(description='Deactualize the advert')
    def make_advert_not_actual(self, request, queryset):
        queryset.update(isActual=False)
        
admin.site.register(Adverts, AdvertsAdmin)