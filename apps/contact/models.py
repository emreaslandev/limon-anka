from django.db import models

class Contact(models.Model):
    name = models.CharField(
        max_length=100, 
        verbose_name='Ad Soyad', 
        help_text='Adınızı ve Soyadınızı giriniz.'
    )
    email = models.EmailField(
        verbose_name='E-Posta Adresi', 
        help_text='Geçerli bir e-posta adresi giriniz.',
        blank=True, 
        null=True
    )
    mobile_phone = models.CharField(
        max_length=20, 
        verbose_name='Cep Telefonu', 
        help_text='Cep telefon numaranızı giriniz.', 
        blank=True, 
        null=True
    )
    phone = models.CharField(
        max_length=20, 
        verbose_name='Telefon Numarası', 
        help_text='Telefon numaranızı giriniz.', 
        blank=True, 
        null=True
    )
    ### url yerine kullanıcı adı kullanılacaksa, ona göre düzenlenebilir.
    instagram = models.URLField(
        max_length=200, 
        verbose_name='Instagram', 
        help_text='Instagram profil URL\'nizi giriniz.', 
        blank=True, 
        null=True
    )
    ### url yerine kullanıcı adı kullanılacaksa, ona göre düzenlenebilir.
    facebook = models.URLField(
        max_length=200, 
        verbose_name='Facebook', 
        help_text='Facebook profil URL\'nizi giriniz.', 
        blank=True, 
        null=True
    )
    ### url yerine kullanıcı adı kullanılacaksa, ona göre düzenlenebilir.
    twitter = models.URLField(
        max_length=200, 
        verbose_name='Twitter', 
        help_text='Twitter profil URL\'nizi giriniz.', 
        blank=True, 
        null=True
    )
    ### url yerine kullanıcı adı kullanılacaksa, ona göre düzenlenebilir.
    linkedin = models.URLField(
        max_length=200, 
        verbose_name='LinkedIn', 
        help_text='LinkedIn profil URL\'nizi giriniz.', 
        blank=True, 
        null=True
    )
    ### url yerine kullanıcı adı kullanılacaksa, ona göre düzenlenebilir.
    youtube = models.URLField(
        max_length=200, 
        verbose_name='Youtube', 
        help_text='Youtube kanal URL\'nizi giriniz.', 
        blank=True, 
        null=True
    )
    ### url yerine kullanıcı adı kullanılacaksa, ona göre düzenlenebilir.    
    tiktok = models.URLField(
        max_length=200, 
        verbose_name='Tiktok', 
        help_text='Tiktok profil URL\'nizi giriniz.', 
        blank=True, 
        null=True
    )
    address = models.CharField(
        max_length=500, 
        verbose_name='Adres', 
        help_text='Adresinizi giriniz.', 
        blank=True, 
        null=True
    )



    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'İletişim'
        verbose_name_plural = 'İletişim Bilgileri'