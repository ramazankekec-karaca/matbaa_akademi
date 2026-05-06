from django import forms
from .models import CustomUser, Soru

class CustomUserCreationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'adi', 'soyadi')

class SoruForm(forms.ModelForm):
    class Meta:
        model = Soru
        fields = [
            'sinif', 'dal', 'ders', 'modul', 'tur', 'soru_metni', 'soru_resmi',
            'secenek_a', 'secenek_b', 'secenek_c', 'secenek_d', 'secenek_e', 
            'dogru_cevap', 'zorluk_seviyesi'
        ]

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Adınız")
    email = forms.EmailField(label="E-posta Adresiniz")
    message = forms.CharField(widget=forms.Textarea, label="Mesajınız")