from django.db import models
from django_ckeditor_5.fields import CKEditor5Field



class About(models.Model):
    title = models.CharField(max_length=100, verbose_name='Başlık')
    content = CKEditor5Field(config_name='extends', verbose_name='İçerik')
    image = models.ImageField(verbose_name='resim', upload_to='about/')
    order = models.IntegerField(default=0, verbose_name='Sıra')
    is_active = models.BooleanField(default=True, verbose_name='Aktif mi?')


    class Meta:
        verbose_name = 'Kurumsal'
        verbose_name_plural = 'Kurumsal'

    def __str__(self):
        return self.title
    