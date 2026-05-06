from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class CustomUser(AbstractUser):
    adi = models.CharField(max_length=50, blank=True, null=True)
    soyadi = models.CharField(max_length=50, blank=True, null=True)
    unvan = models.CharField(max_length=50, blank=True, null=True)
    okul = models.CharField(max_length=255, blank=True, null=True)
    calistigi_alan = models.CharField(max_length=100, blank=True, null=True)
    membership_type = models.CharField(max_length=20, default='free')

    class Meta:
        verbose_name = "Kullanıcı"
        verbose_name_plural = "Kullanıcılar"

class Sinif(models.Model):
    sinif = models.IntegerField(unique=True)

    class Meta:
        verbose_name = "Sınıf"
        verbose_name_plural = "Sınıflar"
        ordering = ['sinif']

    def __str__(self):
        return f"{self.sinif}. Sınıf"

class Dal(models.Model):
    sinif = models.ForeignKey(Sinif, on_delete=models.CASCADE, related_name='dallar')
    adi = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Dal"
        verbose_name_plural = "Dallar"

    def __str__(self):
        return f"{self.sinif.sinif}. Sınıf - {self.adi}"

class Ders(models.Model):
    dal = models.ForeignKey(Dal, on_delete=models.CASCADE, related_name='dersler')
    adi = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Ders"
        verbose_name_plural = "Dersler"

    def __str__(self):
        return self.adi

class Modul(models.Model):
    ders = models.ForeignKey(Ders, on_delete=models.CASCADE, related_name='moduller')
    adi = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Modül"
        verbose_name_plural = "Modüller"

    def __str__(self):
        return self.adi

class SoruTuru(models.Model):
    adi = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Soru Türü"
        verbose_name_plural = "Soru Türleri"

    def __str__(self):
        return self.adi

class Soru(models.Model):
    ZORLUK_SEVIYESI = [('kolay', 'Kolay'), ('orta', 'Orta'), ('zor', 'Zor')]
    ONAY_DURUMLARI = [('taslak', 'Taslak'), ('beklemede', 'Beklemede'), ('onaylandi', 'Onaylandı'), ('reddedildi', 'Reddedildi')]

    sinif = models.ForeignKey(Sinif, on_delete=models.CASCADE)
    dal = models.ForeignKey(Dal, on_delete=models.CASCADE)
    ders = models.ForeignKey(Ders, on_delete=models.CASCADE)
    modul = models.ForeignKey(Modul, on_delete=models.CASCADE)
    tur = models.ForeignKey(SoruTuru, on_delete=models.CASCADE)
    
    soru_metni = models.TextField()
    soru_resmi = models.ImageField(upload_to='soru_resimleri/', blank=True, null=True)
    
    # --- YENİ EKLENEN ALANLAR ---
    cevap_resmi = models.ImageField(upload_to='cevap_resimleri/', blank=True, null=True)
    klasik_cevap = models.TextField(blank=True, null=True)
    # ----------------------------
    
    secenek_a = models.TextField(blank=True, null=True)
    secenek_b = models.TextField(blank=True, null=True)
    secenek_c = models.TextField(blank=True, null=True)
    secenek_d = models.TextField(blank=True, null=True)
    secenek_e = models.TextField(blank=True, null=True)
    
    # GÜNCELLEME: Açık uçlu sorular için boş bırakılabilmesi adına blank=True, null=True eklendi
    dogru_cevap = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], blank=True, null=True)
    
    zorluk_seviyesi = models.CharField(max_length=10, choices=ZORLUK_SEVIYESI, default='orta')
    onay_durumu = models.CharField(max_length=20, choices=ONAY_DURUMLARI, default='onaylandi')
    soruyu_hazirlayan = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Soru"
        verbose_name_plural = "Sorular"

    def __str__(self):
        return self.soru_metni[:50]

class Setting(models.Model):
    key = models.CharField(max_length=100, unique=True)
    value = models.TextField()

    class Meta:
        verbose_name = "Ayar"
        verbose_name_plural = "Ayarlar"

class HataBildirimi(models.Model):
    DURUM_CHOICES = [
        ('yeni', 'Yeni Bekliyor'),
        ('inceleniyor', 'İnceleniyor'),
        ('cozuldu', 'Çözüldü'),
    ]
    
    soru = models.ForeignKey('Soru', on_delete=models.CASCADE, related_name='hata_bildirimleri')
    kullanici = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    mesaj = models.TextField(verbose_name="Hata Detayı")
    durum = models.CharField(max_length=20, choices=DURUM_CHOICES, default='yeni')
    tarih = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Hata Bildirimi - Soru: {self.soru.id} - Durum: {self.durum}"