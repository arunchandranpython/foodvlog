from django.contrib import admin
from .models import categ,prod

class categoryadmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(categ,categoryadmin)

class productadmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'slug','available']
    list_editable = ['stock', 'price']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(prod,productadmin)
