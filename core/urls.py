
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),

    #surprise :)
    path('hello/', views.hello, name='hello'),

    #menu
	path('faq/', views.faq, name='faq'),
	path('contact/', views.contact, name='contact'),

    #error page
	path('error/', views.error, name='error'),

    #regulations
    path('regulations/', views.regulations, name="regulations"),
    path('marketing_regulations/', views.marketing_regulations, name="marketing_regulations"),
    

    #survey sites
    path('survey/<str:product_tag>/', views.new_survey, name="new_survey"),
    path('survey/<str:product_tag>/<str:slug>/', views.survey, name="survey"),

    #products sites
    path('product/<str:req_product>', views.product, name='product'),


    #test site
    path('dev/test/', views.test, name='test')
    

]
