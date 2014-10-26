from django.db import models
from django.template import defaultfilters
import os
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, Adjust

def upload_image_to(instance, filename):
        from django.utils.timezone import now
        filename_base, filename_ext = os.path.splitext(filename)
        return 'images/%s%s%s' % (
            filename_base,
            now().strftime("%Y%m%d%H%M%S"),
            filename_ext.lower(),)

class Proyect(models.Model):
    name_es = models.CharField('Name spanish', max_length=140, null=False, blank=False)
    name_en = models.CharField('Name english', max_length=140, null=True, blank=True)
    location = models.CharField('Location', max_length=140, null=True, blank=True)
    date = models.CharField('Fechas', max_length=140, null=True, blank=True)
    description_es = RichTextField()
    description_en = RichTextField()
    pub_date = models.DateTimeField('Created', editable=False, auto_now_add=True)
    mainImage =  models.ImageField('Main Image', upload_to=upload_image_to, blank=False)
    mainImageBW = ImageSpecField(
                    source='mainImage',
                    processors=[Adjust(color=0.0)],
                    format='JPEG',
                    options={'quality': 100})
    secondImage =  models.ImageField('Second Image', upload_to=upload_image_to, blank=True)
    imageOrientationOpts =  (('left', 'left'), ('rigt', 'right'), ('up', 'up'), ('down', 'down'), ('cntr', 'center'))
    imageOrientation = models.CharField('Alignment', max_length=4, choices=imageOrientationOpts, default='cntr')
    home = models.BooleanField('Home',default=False)
    proyects = models.BooleanField('Proyects',default=False)
    slug = models.SlugField('Slug Name', max_length=100)
    def save(self, *args, **kwargs):
        self.slug = defaultfilters.slugify(self.name_es)
        super(Proyect, self).save(*args, **kwargs)

    def admin_image(self):
        return '<img style="height:100px; width: auto; display: block;" src="%s"/>' % self.mainImage.url
    admin_image.allow_tags = True

    def second_image(self):
        if self.secondImage:
            img = self.secondImage
        else:
            img = self.mainImageBW
        return '<img style="height:100px; width: auto; display: block;" src="%s"/>' % img.url
    second_image.allow_tags = True

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name_es
    class Meta:
        verbose_name = 'Proyect'
        verbose_name_plural = 'Proyects'
    def getGallery(self):
        s = Image.objects.filter(proyect=self).order_by('order')
        return s

class Image(models.Model):
    idImage = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=100, blank=True)
    image =  models.ImageField('Image', upload_to=upload_image_to, blank=True, null=True)
    imageOrientationOpts =  (('left', 'left'), ('rigt', 'right'), ('cntr', 'center'), ('covr', 'cover'))
    imageOrientation = models.CharField('Tipo', max_length=4, choices=imageOrientationOpts, default='covr')
    imageEffectsOptions = (('no','None'),('bw', 'Black & white'), ('one', 'Effect 1'), ('two', 'Effect 2'), ('tre', 'Effect 3'))
    imageEffect = models.CharField('Effect', max_length=4, choices=imageEffectsOptions, default='bw')
    order = models.PositiveSmallIntegerField('Order', blank=False,null=False,default=1)
    blackWhite = ImageSpecField(
        source='image',
        processors=[Adjust(color=0.0)],
        format='JPEG',
        options={'quality': 100})
    effectOne = ImageSpecField(
        source='image',
        processors=[Adjust(brightness=1.45,contrast=1.10,color=0.45)],
        format='JPEG',
        options={'quality': 100})
    effectTwo = ImageSpecField(
        source='image',
         processors=[Adjust(brightness=0.85,contrast=1.30,color=0.45)],
        format='JPEG',
        options={'quality': 100})
    effectThree = ImageSpecField(
        source='image',
        processors=[Adjust(brightness=0.85,contrast=1.25,color=1.20)],
        format='JPEG',
        options={'quality': 100})
    proyect = models.ForeignKey('Proyect')
    def imageWithEffect(self):
        if self.imageEffect == 'no':
            tmpImg = self.image.url
        elif self.imageEffect == 'bw':
            tmpImg = self.blackWhite.url
        elif self.imageEffect == 'one':
            tmpImg = self.effectOne.url
        elif self.imageEffect == 'two':
            tmpImg = self.effectTwo.url
        elif self.imageEffect == 'tre':
            tmpImg = self.effectThree.url
        else:
            tmpImg = self.image.url
        return tmpImg
    def admin_image(self):
        if self.imageEffect == 'no':
            tmpImg = self.image.url
        elif self.imageEffect == 'bw':
            tmpImg = self.blackWhite.url
        elif self.imageEffect == 'one':
            tmpImg = self.effectOne.url
        elif self.imageEffect == 'two':
            tmpImg = self.effectTwo.url
        elif self.imageEffect == 'tre':
            tmpImg = self.effectThree.url
        else:
            tmpImg = self.image.url
        return '<img style="height:100px; width: auto; display: block;" src="%s"/>' % tmpImg
    admin_image.allow_tags = True
    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'
    def __unicode__(self):
        return self.name

class SingleInformation(models.Model):
    aboutImage = models.ImageField('Imagen about', upload_to = upload_image_to,null = False, blank = False)
    aboutText_es = RichTextField()
    aboutText_en = RichTextField()
    line1 = models.CharField('linea 1', max_length=140, null=True, blank=True)
    line2 = models.CharField('linea 2', max_length=140, null=True, blank=True)
    line3 = models.CharField('linea 3', max_length=140, null=True, blank=True)
    line4 = models.CharField('linea 4', max_length=140, null=True, blank=True)
    published = models.BooleanField('Published', default = False)
    def save(self, *args, **kwargs):
        if self.published:
            try:
                temp = SingleInformation.objects.get(published=True)
                if self != temp:
                    temp.published = False
                    temp.save()
            except SingleInformation.DoesNotExist:
                pass
        super(SingleInformation, self).save(*args, **kwargs)
    def admin_Aboutimage(self):
        return '<img style="height:100px; width: auto; display: block;" src="%s"/>' % self.aboutImage.url
    admin_Aboutimage.allow_tags = True
    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"

class Press(models.Model):
    name_es = models.CharField('Name spanish',max_length=140, null=False, blank=False)
    name_en = models.CharField('Name english',max_length=140, null=False, blank=False)
    mainImage = models.ImageField('Main image', upload_to = upload_image_to,null = False, blank = False)
    description_es = RichTextField()
    description_en = RichTextField()
    pub_date = models.DateTimeField('Created', editable=False, auto_now_add=True)
    def admin_image(self):
        return '<img style="height:100px; width: auto; display: block;" src="%s"/>' % self.mainImage.url
    admin_image.allow_tags = True
    class Meta:
        verbose_name = "Elemento de prensa"
        verbose_name_plural = "Elementos de prensa"
