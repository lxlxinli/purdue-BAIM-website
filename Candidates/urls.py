from django.conf.urls import url
from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^$',views.browsecandidates,name="browsecandidates"),
    re_path(r'^test$',views.browse,name="browse")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)