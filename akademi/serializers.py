from rest_framework import serializers
from .models import Sinif, Dal, Ders, Modul

class SinifSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sinif
        fields = '__all__'

class DalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dal
        fields = '__all__'

class DersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ders
        fields = '__all__'

class ModulSerializer(serializers.ModelSerializer):
    # views.py'da hesaplanan zorluk derecelerine göre soru sayılarını API'ye aktarır
    soru_sayilari = serializers.DictField(read_only=True, required=False)
    
    class Meta:
        model = Modul
        fields = '__all__'

class SihirbazModulSerializer(serializers.ModelSerializer):
    soru_sayilari = serializers.DictField(read_only=True, required=False)
    
    class Meta:
        model = Modul
        fields = ['id', 'adi', 'soru_sayilari']