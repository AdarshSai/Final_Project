from django.urls import path
from . import views
from django.views.generic import TemplateView
app_name = "chat"
urlpatterns = [
    path(r'', TemplateView.as_view(template_name='base1.html'), name='base'),
    path(r'nurse', TemplateView.as_view(template_name='Nurse1.html'), name='nurse'),
    path(r'patient', TemplateView.as_view(template_name='Patient.html'), name='patient'),
    path(r'volunteer', TemplateView.as_view(template_name='Volunteer1.html'), name='volunteer'),
    path(r'admin', TemplateView.as_view(template_name='Admin.html'), name='admin'),
    #path(r'chat_script', TemplateView.as_view(template_name='chat_script.html'), name='chat_script'),
    path('chat', views.home, name='home'),
    path('post/', views.post, name='post'),
    path('messages/<str:user_name>', views.messages, name='messages'),
    path(r'patient/<int:user_id>',views.patient_page,name='patient_view'),
    path(r'nurse/<int:user_id>',views.nurse_page,name='nurse_view'),
    path(r'volunteer/<int:user_id>',views.volunteer_page,name='volunteer_view'),
    path('upload/', views.upload, name='views.upload'),
    path('ml/',views.heart_Ml_Pred, name='ml'),
    path('about_us/',TemplateView.as_view(template_name='about_us1.html'),name='about_us'),
    path('bot',TemplateView.as_view(template_name='bot/in.html'),name='bot'),
    path(r'login/', views.user_login, name='login'),
    path(r'logout/', views.user_logout, name='logout'),
    path(r'home/', views.home, name='home'),
    path(r'about/', views.about, name='about'),
    path(r'regi/', views.register, name='register'),
    path(r'register/patient', views.registerpatient, name='register_patient'),
    path(r'register/volunteer', views.registervolunteer, name='register_volunteer'),
]

