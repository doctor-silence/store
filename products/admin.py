from django.contrib import admin

from products.models import Basket, Product, ProductCategory

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')  # Отображение таблицы в админке
    fields = ('name', 'description', 'price', 'quantity', 'image', 'stripe_products_price_id', 'category')  #Отображение внутри оъекта
    readonly_fields = ('description',)  # Поле только для чтения
    search_fields = ('name',)   # Поиск по нужному полю
    ordering = ('name',)   # Сортировка в алфовитном порядке


class BasketAdmin(admin.TabularInline):    #Связываем карзину и пользователя в админке
    model = Basket
    fields = ('product', 'quantity')
    extra = 0   # Значения полей которые отображаются в админке User
