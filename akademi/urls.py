from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Ana Sayfa ve Temel Linkler
    path('', views.home, name='home'),
    path('sorubankasi/', views.soru_bankasi, name='soru_bankasi'),
    path('sihirbaz/', views.sinav_sihirbazi, name='sihirbaz'),
    path('panel/', views.panel, name='panel'),
    path('yeni-soru/', views.yeni_soru, name='yeni_soru'),
    path('hakkinda/', views.about, name='about'),
    path('iletisim/', views.contact_view, name='contact'),
    path('api/toggle-exam-question/', views.toggle_exam_question, name='toggle_exam_question'),
    path('manuel-sinav/', views.manuel_sinav_kagit, name='manuel_sinav_kagit'),
    path('sinavi-temizle/', views.clear_exam_session, name='clear_exam_session'),
    path('api/hata-bildir/', views.hata_bildir, name='hata_bildir'),
    path('api/export-word/', views.export_word, name='export_word'),
    
    # Üyelik İşlemleri
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    
    # API / AJAX (Soru filtreleme ve sihirbaz için arka plan işlemleri)
    path('api/filtered-sorular/', views.get_filtered_sorular, name='get_filtered_sorular'),
    path('api/get-siniflar/', views.get_siniflar, name='get_siniflar'),
    path('api/dallar/<int:sinif_id>/', views.get_dallar, name='get_dallar'),
    path('api/dersler/<int:dal_id>/', views.get_dersler, name='get_dersler'),
    path('api/moduller/<int:ders_id>/', views.get_moduller, name='get_moduller'),
    
    # Yeni soru ekleme (Bulk ve Manual) işlemleri
    path('yeni-soru-bulk/', views.yeni_soru_bulk, name='yeni_soru_bulk'),
    path('yeni-soru-manual/', views.yeni_soru_manual, name='yeni_soru_manual'),
    path('api/upload-answer-image/', views.upload_answer_image, name='upload_answer_image'),

    path('yeni-soru/', views.yeni_soru, name='yeni_soru'),
    
    # YENİ EKLENEN SATIR: Soru Düzenleme Bağlantısı
    path('soru-duzenle/<int:soru_id>/', views.soru_duzenle, name='soru_duzenle'),
]