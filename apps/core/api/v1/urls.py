from django.urls import path, include

urlpatterns = [
    path('accounts/', include('apps.accounts.api.v1.urls')),
    path('cart/', include('apps.cart.api.v1.urls')),
    path('dashboard/', include('apps.dashboard.api.v1.urls')),
    path('order/', include('apps.order.api.v1.urls')),
    path('payment/', include('apps.payment.api.v1.urls')),
    path('review/', include('apps.review.api.v1.urls')),
    path('shop/', include('apps.shop.api.v1.urls')),
    path('shop/', include('apps.shop.api.v1.urls')),
    path('website/', include('apps.website.api.v1.urls')),
]
