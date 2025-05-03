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


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Başlık')
    paragraph_1 = CKEditor5Field(config_name='extends', verbose_name='Paragraf 1')
    paragraph_2 = CKEditor5Field(config_name='extends', verbose_name='Paragraf 2')
    cover_image = models.ImageField(upload_to='blogs/covers/', verbose_name='Kapak Resmi')
    category = models.ForeignKey(Category, related_name='blogs', on_delete=models.CASCADE, verbose_name='Kategori')
    is_active = models.BooleanField(default=True, verbose_name='Aktif mi?')
    order = models.IntegerField(default=0, verbose_name='Sıra')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Güncellenme Tarihi')
    slug = models.SlugField(blank=True, unique=True, editable=False)    



    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog İçerikleri'


    def __str__(self):
        return self.title
    

class Media(models.Model):
    blog_media = models.ForeignKey(Blog, related_name='media', on_delete=models.CASCADE, verbose_name='Blog Medyası')
    file = models.FileField(upload_to='blogs/media/', verbose_name='Dosya')
    MEDIA_TYPE_CHOICES = (
        ('img', 'resim'),
        ('vid', 'video'),
    )
    media_type = models.CharField(max_length=5, choices=MEDIA_TYPE_CHOICES, verbose_name='Medya Türü')

    def __str__(self):
        return f"Media for {self.blog_media.title}"

    def is_image(self):
        return self.media_type == 'img'

    def is_video(self):
        return self.media_type == 'vid'

    class Meta:
        verbose_name = 'Blog Medyası'
        verbose_name_plural = 'Blog Medyaları'