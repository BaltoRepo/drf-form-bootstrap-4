from django.urls import path
from . import views

urlpatterns = [
    path('', views.DemoForms.as_view(), name='root'),
]
