from django.contrib import admin
from graphs.models import posters, papers
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.
@admin.register(posters)
@admin.register(papers)

class ViewAdmin(ImportExportModelAdmin):
    pass
