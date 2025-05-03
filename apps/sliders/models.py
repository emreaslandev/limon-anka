from django.db import models

class Slider (models.Model):
    title = models.CharField(max_length=100, verbose_name='Başlık')
    description = models.TextField(verbose_name='Açıklama')
    image = models.ImageField(upload_to='sliders/', verbose_name='Resim')
    order = models.IntegerField(default=0, verbose_name='Sıra')
    is_active = models.BooleanField(default=True, verbose_name='Aktif mi?')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Başlık'
        verbose_name_plural = 'Başlıklar'
