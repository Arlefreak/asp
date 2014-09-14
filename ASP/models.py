# -*- coding: utf-8 -*-
from django.db import models
from ckeditor.fields import RichTextField
import os

def upload_image_to(instance, filename):
		from django.utils.timezone import now
		filename_base, filename_ext = os.path.splitext(filename)
		return 'images/%s%s%s' % (
			filename_base,
			now().strftime("%Y%m%d%H%M%S"),
			filename_ext.lower(),)

class singleInformation(models.Model):
	aboutImage = models.ImageField('Imagen about', upload_to = upload_image_to,null = False, blank = False)
	aboutText = RichTextField()
	line1 = models.CharField('linea 1', max_length=140, null=True, blank=True)
	line2 = models.CharField('linea 2', max_length=140, null=True, blank=True)
	line3 = models.CharField('linea 3', max_length=140, null=True, blank=True)
	line4 = models.CharField('linea 4', max_length=140, null=True, blank=True)
	published = models.BooleanField('Publicado', default = False)
	def save(self, *args, **kwargs):
		if self.published:
			try:
				temp = singleInformation.objects.get(published=True)
				if self != temp:
					temp.published = False
					temp.save()
			except singleInformation.DoesNotExist:
				pass
		super(singleInformation, self).save(*args, **kwargs)
	def admin_Aboutimage(self):
		return '<img style="height:100px; width: auto; display: block;" src="%s"/>' % self.aboutImage.url
	admin_Aboutimage.allow_tags = True
	class Meta:
		verbose_name = "About"
		verbose_name_plural = "About"

class Press(models.Model):
	name = models.CharField(max_length=140, null=False, blank=False)
	mainImage = models.ImageField('Imagen principal', upload_to = upload_image_to,null = False, blank = False)
	description = RichTextField()
	def admin_image(self):
		return '<img style="height:100px; width: auto; display: block;" src="%s"/>' % self.mainImage.url
	admin_image.allow_tags = True
	class Meta:
		verbose_name = "Elemento de prensa"
		verbose_name_plural = "Elementos de prensa"