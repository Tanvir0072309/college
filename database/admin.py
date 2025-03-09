from django.contrib import admin
from .models import Class, Subject,Signup_user, Student_profile, AdmissionForm,ExamMarks,Faculty
from import_export.admin import ImportExportModelAdmin
admin.site.register(Signup_user)


admin.site.register(ExamMarks)
admin.site.register(Class)
admin.site.register(Subject)
admin.site.register(Faculty)
class studentDetails(ImportExportModelAdmin,admin.ModelAdmin):
    ...
admin.site.register(Student_profile,studentDetails)


class studentadmission(ImportExportModelAdmin,admin.ModelAdmin):
    ...
admin.site.register(AdmissionForm,studentadmission)