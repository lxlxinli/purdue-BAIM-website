from django.conf.urls import url
from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "Candidates"

urlpatterns = [
    re_path(r'^$',views.browsecandidates,name="browsecandidates"),
    re_path(r'^test$',views.browse,name="browse"),
    re_path(r'^achievements',views.achievements,name="achievements"),
    re_path(r'^programdetails',views.programdetails,name="programdetails")
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)