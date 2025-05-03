from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Kategori Adı')
    order = models.PositiveIntegerField(default=0, verbose_name='Sıra')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'

class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="Ürün Adı")
    description = CKEditor5Field(config_name='extends', verbose_name="Açıklama")
    cover_image = models.ImageField(upload_to='products/covers/', verbose_name='Kapak Resmi')
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Kategori')
    is_active = models.BooleanField(default=True, verbose_name='Aktif mi?')
    slug = models.SlugField(blank=True, unique=True, editable=False)    
    order = models.IntegerField(verbose_name="Sıra", default=0)

    class Meta:
        verbose_name = 'Ürün'
        verbose_name_plural = 'Ürünler'


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Media(models.Model):
    product_media = models.ForeignKey(Product, related_name='media', on_delete=models.CASCADE, verbose_name='Ürün Medyası')
    file = models.FileField(upload_to='products/media/', verbose_name='Dosya')
    MEDIA_TYPE_CHOICES = (
        ('img', 'resim'),
        ('vid', 'video'),
    )
    media_type = models.CharField(max_length=5, choices=MEDIA_TYPE_CHOICES, verbose_name='Medya Türü')

    def __str__(self):
        return f"Media for {self.product_media.title}"

    def is_image(self):
        return self.media_type == 'img'

    def is_video(self):
        return self.media_type == 'vid'

    class Meta:
        verbose_name = 'Ürün Medyası'
        verbose_name_plural = 'Ürün Medyaları'
    
