
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('questionnaire/', views.questionnaire, name='questionnaire'),
    path('questionnaire/basic/', views.questionnaire_basic, name='questionnaire_basic'),
    path('questionnaire/injury/', views.questionnaire_injury, name='questionnaire_injury'),
    path('hello/', views.hello, name='hello'),
	path('faq/', views.faq, name='faq'),
	path('contact/', views.contact, name='contact'),
	path('error/', views.error, name='error'),
    path('regulations/', views.regulations, name="regulations"),
    path('marketing_regulations/', views.marketing_regulations, name="marketing_regulations"),
]
