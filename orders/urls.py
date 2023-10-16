
from django.urls import path
from . import views
from orders.views import order, payment

urlpatterns = [
    path('', views.order, name='order'),
    path('<int:order_id>/', order, name='order'),
    path('payment/<int:order_id>/', payment, name='payment'),
    path('payment/success/', views.payment_success, name='paymentsuccess')
]
