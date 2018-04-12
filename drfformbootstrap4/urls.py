from django.urls import path
from . import views

urlpatterns = [
    path('', views.Forms.as_view(), name='root'),
]
