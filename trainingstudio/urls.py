from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from scripts.bot import HostBot


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('accounts/',include('accounts.urls')),
    path('orders/',include('orders.urls')),
    path('reflink/',include('promotions.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "Training administration"
admin.site.index_title = "You can change what you can"
admin.site.site_title = "Custom Training"

#bot request if server start
HostBot()
