from django.contrib import admin
from Candidates.models import student
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.
@admin.register(student)
class ViewAdmin(ImportExportModelAdmin):
    pass

class StudentInformation(resources.ModelResource):
    class Meta:
        model = student
        import_id_fields = ['student_id']