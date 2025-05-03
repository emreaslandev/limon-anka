from django.db import models

class Gallery(models.Model):
    MEDIA_TYPES = (
        ('img', 'Resim'),
        ('vid', 'Video'),
    )

    file = models.FileField(upload_to='galeri/', verbose_name="Dosya")
    type = models.CharField(max_length=5, choices=MEDIA_TYPES, verbose_name="Tip")
    # title = models.CharField(max_length=255, verbose_name='Başlık', blank=True, null=True)
    order = models.IntegerField(verbose_name='Sıra', default=0)
    is_active = models.BooleanField(default=True, verbose_name='Aktif mi?')


    class Meta:
        verbose_name = 'İçerik'
        verbose_name_plural = 'İçerikler'

    def __str__(self):
        return f"İçerik:{self.id} - {self.type}"
