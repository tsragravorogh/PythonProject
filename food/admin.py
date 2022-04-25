from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from django import forms
from food.models import Food, Country, TypeFood, Brand
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class DescriptionAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Food
        fields = '__all__'


class FoodAdmin(admin.ModelAdmin):
    list_display = ('brand', 'price', 'date', 'description', 'weight', 'get_image')
    list_display_links = ('brand', 'description',)
    list_filter = ('date', 'brand',)
    search_fields = ('description',)
    readonly_fields = ('price', 'get_image',)
    list_editable = ('price',)
    form = DescriptionAdminForm

    fieldsets = (
        (None, {
            'fields': (('brand', 'price',),)
        }),
        ('Описание и цена', {
            # 'classes': ('collapse', ),
            'fields': (('description',),)
        }),
        ('Фото', {
            'fields': (('image', 'get_image'),)
        })
    )

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src={obj.image.url} height="50" width="50">')
        else:
            return ''


admin.site.register(Food, FoodAdmin)
admin.site.register(Country)
admin.site.register(TypeFood)
admin.site.register(Brand)