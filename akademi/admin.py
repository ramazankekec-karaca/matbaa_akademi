from django.contrib import admin
from django import forms # YENİ: Her kutuya özel boyut vermek için eklendi
from .models import Sinif, Dal, Ders, Modul, SoruTuru, Soru, CustomUser, Setting, HataBildirimi

# YENİ: Soru modeline özel form oluşturup boyutları ince ayarla belirliyoruz
class SoruAdminForm(forms.ModelForm):
    class Meta:
        model = Soru
        fields = '__all__'
        widgets = {
            # Soru metni ve klasik cevap geniş ve 3 satır
            'soru_metni': forms.Textarea(attrs={'rows': 2, 'style': 'width: 60%;'}),
            'klasik_cevap': forms.Textarea(attrs={'rows': 2, 'style': 'width: 60%;'}),
            
            # Seçenekler (Şıklar) çok daha dar (%40) ve sadece 1 satır
            'secenek_a': forms.Textarea(attrs={'rows': 1, 'style': 'width: 40%;'}),
            'secenek_b': forms.Textarea(attrs={'rows': 1, 'style': 'width: 40%;'}),
            'secenek_c': forms.Textarea(attrs={'rows': 1, 'style': 'width: 40%;'}),
            'secenek_d': forms.Textarea(attrs={'rows': 1, 'style': 'width: 40%;'}),
            'secenek_e': forms.Textarea(attrs={'rows': 1, 'style': 'width: 40%;'}),
        }

@admin.register(Soru)
class SoruAdmin(admin.ModelAdmin):
    form = SoruAdminForm # Yukarıdaki özel boyutu buraya bağladık
    
    list_display = ('soru_metni_ozet', 'sinif', 'ders', 'zorluk_seviyesi', 'onay_durumu')
    list_filter = ('onay_durumu', 'sinif', 'ders', 'zorluk_seviyesi')
    search_fields = ('soru_metni', 'klasik_cevap')
    
    fieldsets = (
        ('Hiyerarşi', {'fields': ('sinif', 'dal', 'ders', 'modul')}),
        ('İçerik', {'fields': ('tur', 'zorluk_seviyesi', 'soru_metni', 'soru_resmi')}),
        ('Seçenekler ve Cevaplar', {'fields': (
            ('secenek_a', 'secenek_b'), 
            ('secenek_c', 'secenek_d'), 
            'secenek_e', 
            'dogru_cevap',
            'klasik_cevap', 
            'cevap_resmi'   
        )}),
        ('Yönetim', {'fields': ('soruyu_hazirlayan', 'onay_durumu')}),
    )

    def soru_metni_ozet(self, obj):
        return obj.soru_metni[:50] + "..." if len(obj.soru_metni) > 50 else obj.soru_metni
    soru_metni_ozet.short_description = "Soru Metni"

@admin.register(Sinif)
class SinifAdmin(admin.ModelAdmin):
    list_display = ('sinif', '__str__')

@admin.register(HataBildirimi)
class HataBildirimiAdmin(admin.ModelAdmin):
    list_display = ('soru', 'kullanici', 'durum', 'tarih')
    list_filter = ('durum', 'tarih')
    search_fields = ('mesaj',)

admin.site.register(Dal)
admin.site.register(Ders)
admin.site.register(Modul)
admin.site.register(SoruTuru)
admin.site.register(CustomUser)
admin.site.register(Setting)