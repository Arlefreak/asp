from django.contrib import admin
from models import *
from embed_video.admin import AdminVideoMixin

# Register your models here.
class ImageInline(admin.TabularInline):
    model = Image
    verbose_name_plural = 'Images'
    extra = 1

class VideoInline(admin.TabularInline):
    model = Video
    verbose_name_plural = 'Videos'
    extra = 1

class singleInformationAdmin(admin.ModelAdmin):
	list_display = ('admin_Aboutimage', 'aboutText_es', 'published',)
	list_display_links = ('admin_Aboutimage', 'aboutText_es',)
	list_editable = ('published',)
	ordering = ('id',)

class proyectAdmin(admin.ModelAdmin):
	fields = ['order', 'name_es', 'name_en', 'location', 'date','description_es', 'description_en', 'mainImage', 'secondImage', 'imageOrientation', 'home', 'proyects', 'socialText_es', 'socialText_en']
	list_display = ('name_es', 'admin_description', 'admin_image', 'second_image', 'imageOrientation', 'home', 'proyects', 'pub_date', 'order')
	list_display_links = ('name_es', 'admin_image', 'pub_date')
	list_editable = ('imageOrientation', 'home', 'proyects', 'order')
        inlines = [ImageInline, VideoInline]
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

class videoAdmin(AdminVideoMixin, admin.ModelAdmin):
	list_display = ('name', 'order', 'proyect')
	list_display_links = ('name', 'proyect')
	ordering = ('order',)
	list_editable = ('order',)

admin.site.register(SingleInformation, singleInformationAdmin)
admin.site.register(Proyect, proyectAdmin)
admin.site.register(Image, imageAdmin)
admin.site.register(Press, pressAdmin)
admin.site.register(Video, videoAdmin)
