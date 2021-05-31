from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('List', views.List, name="List"),
    path('Contact', views.contactus, name="Contact"),
    path('Search', views.search, name="Search"),
    path('Product/BuyNow/<str:myid>', views.buynow, name="BuyNow"),
    path('About', views.about, name="About"),
    path('Checkout', views.checkout, name="Checkout"),
    path('Track/<int:myid>', views.track, name="Tracker"),
    path('Tracker', views.tracker, name="Track"),
    path('Payment/<int:myid>', views.payment, name="Payment"),
    path("Product/<str:myid>", views.productview, name="ProductView"),
]
