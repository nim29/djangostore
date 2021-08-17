from django.urls import path
from . import views

app_name="perfumes"

urlpatterns = [
    path('perfumes/', views.perfumes),
	path('perfumes/checkout/', views.checkout, name="checkout"),
]