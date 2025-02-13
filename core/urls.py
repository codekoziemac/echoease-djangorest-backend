
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static

urlpatterns = [
    path('myadmin/',include('custom_admin.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('djoser.urls')),
    path('api/', include('users.urls')),
    path('api/artists/', include('artists.urls')),
    path('api/chat/', include('chat.urls')),
    path('api/bookings/', include('booking.urls')),
    path('api/payments/', include('payment.urls')),
    path('api/disputes/', include('dispute.urls')),
    path('api/notifications/', include('notification.urls')),
    path('api/schedule/', include('schedule.urls')),
    path('api/transactions/', include('transaction.urls')),
    path('api/reviews/', include('review.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
