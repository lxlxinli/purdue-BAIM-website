from django.conf.urls import url
from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "graphs"

urlpatterns = [
    re_path(r'^paperimage',views.paperimage,name='paperimage'),
    re_path(r'^posterimage',views.posterimage,name='posterimage')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)