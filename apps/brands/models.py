from django.db import models

class Brand(models.Model):
    title = models.CharField(max_length=500, verbose_name="Marka Adı", help_text="Markanın adını girin.")
    logo = models.ImageField(upload_to="media/brands", verbose_name="Marka Logosu", help_text="Markanın logosunu girin.")
    order = models.IntegerField(default=0, verbose_name="Sıra")
    is_active = models.BooleanField(default=True, verbose_name='Aktif mi?')


    class Meta:
        verbose_name = "Marka"
        verbose_name_plural = "Markalar"

    def __str__(self):
        return self.title