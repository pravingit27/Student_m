from django.contrib import admin

from vertos import models

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("pk","username","email","phone_num","gender","age","user_type")

admin.site.register(models.User,UserAdmin)

admin.site.register(models.School)
admin.site.register(models.Section)

class StudentAdmin(admin.ModelAdmin):
    list_display = ("pk","student","school","roll_num")

admin.site.register(models.Student,StudentAdmin)

admin.site.register(models.Standard)
admin.site.register(models.Major)
admin.site.register(models.Class_Details)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ("pk","title","subject_major")

admin.site.register(models.Subject,SubjectAdmin)

class StaffAdmin(admin.ModelAdmin):
    list_display = ("pk","staff","school","designation")
    
admin.site.register(models.Staff,StaffAdmin)
admin.site.register(models.Teaching_Staff_Details)

class ExamAdmin(admin.ModelAdmin):
    list_display = ("pk","category","school","start_date","end_date")

admin.site.register(models.Exam,ExamAdmin)
admin.site.register(models.Exam_Category)

class ResultAdmin(admin.ModelAdmin):
    list_display = ("pk","exam_name","student_name","subject_name","marks")

admin.site.register(models.Result,ResultAdmin)
