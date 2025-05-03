from django.db import models

class Testimonial(models.Model):
    type = models.CharField(
        max_length=90,
        verbose_name="Tip",
        help_text="Resim veya metin seçin.",
        choices=[("img", "Resim"), ("txt", "Metin")]
    )

    text = models.TextField(
        max_length=4000,
        verbose_name="Metin",
        help_text="Metin seçtiyseniz metni girin.",
        blank=True,
    )

    image = models.ImageField(
        verbose_name="Resim",
        upload_to="media/testimonials",
        help_text="Resim seçtiyseniz resmi girin.",
        null=True,
        blank=True,
    )

    author = models.CharField(
        verbose_name="Yazar",
        help_text="Yorumu yapan kişinin ismi. (Resim seçtiyseniz gözükmeyecek.)",
        max_length=300,
    )

    role = models.CharField(
        verbose_name="Rol",
        help_text="Örn. Müşteri, Müteahhit...",
        max_length=400,
    )

    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True, verbose_name='Aktif mi?')

    class Meta:
        verbose_name = "Müşteri Yorumu"
        verbose_name_plural = "Müşteri Yorumları"

    def __str__(self):
        return self.author