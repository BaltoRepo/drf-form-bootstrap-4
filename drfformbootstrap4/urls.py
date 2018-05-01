from django.urls import path
from . import views
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls import include, url

urlpatterns = [
    path(
        '',
        TemplateView.as_view(template_name="drfformbootstrap4/demo/root.html"),
        name='root'
    ),
    path('vertical', views.DemoVertical.as_view(), name='vertical'),
    path('horizontal', views.DemoHorizontal.as_view(), name='horizontal'),
    path('inline', views.DemoInline.as_view(), name='inline'),
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
