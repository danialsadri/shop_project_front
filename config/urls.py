from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.core.api.v1.urls')),
    path('', include('apps.website.urls', namespace='website')),
    path('dashboard/', include('apps.dashboard.urls', namespace='dashboard')),
    path('accounts/', include('apps.accounts.urls', namespace='accounts')),
    path('shop/', include('apps.shop.urls', namespace='shop')),
    path('cart/', include('apps.cart.urls', namespace='cart')),
    path('order/', include('apps.order.urls', namespace='order')),
    path('payment/', include('apps.payment.urls', namespace='payment')),
    path('review/', include('apps.review.urls', namespace='review')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.SHOW_DEBUGGER_TOOLBAR:
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls'))]

admin.sites.AdminSite.site_header = 'پنل مدیریت'
admin.sites.AdminSite.site_title = 'پنل مدیریت'
admin.sites.AdminSite.index_title = 'پنل مدیریت'

handler400 = "config.error_views.error_400"
handler403 = "config.error_views.error_403"
handler404 = "config.error_views.error_404"
handler500 = "config.error_views.error_500"
