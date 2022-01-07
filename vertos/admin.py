from django.contrib import admin


from vertos import models

# Register your models here.


admin.site.register(models.User)
admin.site.register(models.School)
admin.site.register(models.Section)
admin.site.register(models.Student)
admin.site.register(models.Standard)
admin.site.register(models.Major)
admin.site.register(models.Class_Details)
admin.site.register(models.Subject)
admin.site.register(models.Staff)
admin.site.register(models.Teaching_Staff_Details)
admin.site.register(models.Exam)
admin.site.register(models.Exam_Category)
admin.site.register(models.Result)
