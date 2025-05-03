from django.db import models

class Stat(models.Model):
    title = models.CharField(max_length=100)
    value = models.IntegerField()
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True, verbose_name='Aktif mi?')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'İstatistik'
        verbose_name_plural = 'İstatistikler'
