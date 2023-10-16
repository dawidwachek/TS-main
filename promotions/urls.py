
from django.urls import path
from . import views
from promotions.views import reflink

urlpatterns = [
    path('<int:ref_id>/', reflink, name='reflink'),
    path('banners/', views.banner, name='banner'),

]
