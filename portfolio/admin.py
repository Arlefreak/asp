from django.contrib import admin
from models import *
# Register your models here.
class ImageInline(admin.StackedInline):
    model = Image
    verbose_name_plural = 'Images'
    extra = 1

class singleInformationAdmin(admin.ModelAdmin):
	list_display = ('admin_Aboutimage', 'aboutText_es', 'published',)
	list_display_links = ('admin_Aboutimage', 'aboutText_es',)
	list_editable = ('published',)
	ordering = ('id',)

class proyectAdmin(admin.ModelAdmin):
	fields = ['order', 'name_es', 'name_en', 'location', 'date','description_es', 'description_en', 'mainImage', 'secondImage', 'imageOrientation', 'home', 'proyects', 'socialText_es', 'socialText_en']
	list_display = ('name_es', 'description_es', 'admin_image', 'second_image', 'imageOrientation', 'home', 'proyects', 'pub_date', 'order')
	list_display_links = ('name_es', 'description_es', 'admin_image', 'pub_date')
	list_editable = ('imageOrientation', 'home', 'proyects', 'order')
        inlines = [ImageInline]
        ordering = ('pub_date',)

class imageAdmin(admin.ModelAdmin):
	list_display = ('name', 'admin_image', 'imageOrientation', 'proyect', 'imageEffect', 'order')
	list_display_links = ('name', 'admin_image', 'proyect')
	list_editable = ('imageOrientation', 'imageEffect', 'order')
	ordering = ('proyect',)
	list_filter = ('proyect',)

class pressAdmin(admin.ModelAdmin):
	list_display = ('name_es', 'admin_image', 'description_es', 'pub_date')
	list_display_links = ('name_es', 'admin_image', 'description_es', 'pub_date')
	ordering = ('pub_date',)

admin.site.register(SingleInformation, singleInformationAdmin)
admin.site.register(Proyect, proyectAdmin)
admin.site.register(Image, imageAdmin)
admin.site.register(Press, pressAdmin)
