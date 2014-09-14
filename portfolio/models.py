from django.db import models
from django.template import defaultfilters
import os
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


def upload_image_to(instance, filename):
        from django.utils.timezone import now
        filename_base, filename_ext = os.path.splitext(filename)
        return 'images/%s%s%s' % (
            filename_base,
            now().strftime("%Y%m%d%H%M%S"),
            filename_ext.lower(),)

class Proyect(models.Model):
    name_es = models.CharField('Name', max_length=140)
    name_en = models.CharField('Name', max_length=140)
    description_es = RichTextField()
    description_en = RichTextField()
    pub_date = models.DateTimeField('Created', editable=False, auto_now_add=True)
    mainImage =  models.ImageField('Main Image', upload_to=upload_image_to, blank=False)
    secondImage =  models.ImageField('Second Image', upload_to=upload_image_to, blank=True)
    imageOrientationOpts =  (('left', 'left'), ('rigt', 'right'), ('up', 'up'), ('down', 'down'), ('cntr', 'center'))
    imageOrientation = models.CharField('Tipo', max_length=4, choices=imageOrientationOpts, default='cntr')
    published = models.BooleanField('Published',default=False)
    slug = models.SlugField('Slug Name', max_length=100)
    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.name)
        super(Proyect, self).save(*args, **kwargs)

    def admin_image(self):
        return '<img style="height:100px; width: auto; display: block;" src="%s"/>' % self.mainImage.url
    admin_image.allow_tags = True

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Proyect'
        verbose_name_plural = 'Proyects'
    def getGallery(self):
        s = Image.objects.filter(proyect=self, img_type='gal')
        return s

class Image(models.Model):
    idImage = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', max_length=100, blank=True)
    image =  models.ImageField('Imagen', upload_to=upload_image_to, blank=True, null=True)
    imageOrientationOpts =  (('left', 'left'), ('rigt', 'right'), ('up', 'up'), ('down', 'down'), ('cntr', 'center'), ('covr', 'cover'))
    imageOrientation = models.CharField('Tipo', max_length=4, choices=imageOrientationOpts, default='covr')
    proyect = models.ForeignKey('Proyect')
    def admin_image(self):
        return '<img style="height:100px; width: auto; display: block;" src="%s"/>' % str(self.blob.url)
    admin_image.allow_tags = True
    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'

    def __unicode__(self):
        return self.name

class singleInformation(models.Model):
    aboutImage = models.ImageField('Imagen about', upload_to = upload_image_to,null = False, blank = False)
    aboutText_es = RichTextField()
    aboutText_en = RichTextField()
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
    name_es = models.CharField(max_length=140, null=False, blank=False)
    name_en = models.CharField(max_length=140, null=False, blank=False)
    mainImage = models.ImageField('Imagen principal', upload_to = upload_image_to,null = False, blank = False)
    description_es = RichTextField()
    description_en = RichTextField()
    pub_date = models.DateTimeField('Created', editable=False, auto_now_add=True)
    def admin_image(self):
        return '<img style="height:100px; width: auto; display: block;" src="%s"/>' % self.mainImage.url
    admin_image.allow_tags = True
    class Meta:
        verbose_name = "Elemento de prensa"
        verbose_name_plural = "Elementos de prensa"