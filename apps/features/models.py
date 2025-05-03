from django.db import models

class Feature(models.Model):
    title = models.CharField(max_length=100, verbose_name="Başlık")
    description = models.TextField(verbose_name="Açıklama")
    icon = models.CharField(max_length=50, blank=True, null=True, verbose_name="ikon")
    order = models.IntegerField(verbose_name='Sıra', default=0)
    is_active = models.BooleanField(default=True, verbose_name='Aktif mi?')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Özellik'
        verbose_name_plural = 'Özellikler'