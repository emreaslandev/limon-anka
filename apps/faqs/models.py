from django.db import models

class Faq(models.Model):
    question = models.TextField(verbose_name='Soru')
    answer = models.TextField(verbose_name='Cevap')
    order = models.IntegerField(verbose_name='Sıra', default=0)
    is_active = models.BooleanField(default=True, verbose_name='Aktif mi?')

    class Meta:
        verbose_name = 'S.S.S'
        verbose_name_plural = 'S.S.S'


    def __str__(self):
        return f"{self.id} - numaralı soru"