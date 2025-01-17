"""
URL configuration for laced project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from . import settings
from core import views as core_views
from users import views as user_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", core_views.home_view, name="home"),
    path("login/", user_views.login_view, name="login"),
    path("logout/", user_views.logout_view, name="logout"),
    path("signup/", user_views.signup_view, name="signup"),
    path("account/", core_views.account_view, name="account"),
    path("account/addresses/", user_views.account_addresses_view, name="account_addresses"),
    path("account/orders/", core_views.account_orders_view, name="account_orders"),
    path("account/favourites/", core_views.account_favourites_view, name="account_favourites"),
    path("products/", core_views.products_view, name="products"),
    path(
        "products/<int:product_id>/",
        core_views.product_detail_view,
        name="product_detail",
    ),
    path("products/add_to_cart/", core_views.add_to_cart, name="add_to_cart"),
    path("cart/", core_views.cart_view, name="cart"),
    path("cart/update_cart_quantity/<int:cart_item_id>/<int:quantity>/", core_views.update_cart_quantity, name="update_cart_quantity"),
    path("cart/remove_from_cart/<int:cart_item_id>/", core_views.remove_from_cart, name="delete_cart_item"),
    path(
        "products/<int:product_id>/favourite/",
        core_views.add_remove_user_favourite,
        name="favourite",
    ),
    path("checkout/", core_views.checkout_view, name="checkout"),
    path("create_payment_intent/", core_views.create_payment, name="create_payment_intent"),
    path("__debug__/", include("debug_toolbar.urls")),
]

# USED TO SERVE MEDIA FILES IN DEVELOPMENT
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
