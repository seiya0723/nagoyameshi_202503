"""
URL configuration for nagoyameshi_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from nagoyameshi import views

#画像関連
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),

    path("", views.TopView.as_view(), name="top" ),
    path("detail/<int:pk>/", views.RestaurantDetailView.as_view(), name="detail"),
    path("detail/new/", views.ReviewCreateView.as_view(), name="new"),
    path("detail/favorite/", views.FavoriteCreateView.as_view(), name="favorite"),
    path("detail/reservation", views.ReservationCreateView.as_view(), name="reservation"),
    path("mypage/", views.MypageView.as_view(), name="mypage"),
    path("mypage/favorite/", views.FavoriteListView.as_view(), name="favorite_list"),
    path("mypage/reservation/", views.ReservationListView.as_view(), name="reservation_list"),

    path("checkout/", views.CheckoutView.as_view(), name="checkout"),
    path("success/", views.SuccessView.as_view(), name="success"),
    path("portal/", views.PortalView.as_view(), name="portal"),
]

#画像関連
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
