from django.core import validators
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.aggregates import Count
from django.db.models.signals import post_save, pre_save
from django.dispatch.dispatcher import receiver
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator,MinValueValidator
from django.db.models import Q
from rest_framework.compat import distinct

# Create your models here.
class SchoolBaseModel(models.Model):
    status = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey('User',related_name='+',on_delete=models.CASCADE,null=True)
    updated_by = models.ForeignKey('User',related_name='+',on_delete=models.CASCADE,null=True)
    deleted_by = models.ForeignKey('User',related_name='+',on_delete=models.CASCADE,null=True)

    class Meta:
        abstract = True

    def soft_delete(self):
        self.deleted = True
        self.status = False
        self.save()

class User(SchoolBaseModel,AbstractUser):
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(max_length=250,unique=True)
    first_name = models.CharField(max_length=50,blank=True,null=True)
    last_name = models.CharField(max_length=50,blank=True,null=True)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('NA','Others')
    )

    gender = models.CharField(max_length=10,choices=GENDER_CHOICES,default='NA')
    phone_num = models.CharField(max_length=15,unique=True)
    age = models.IntegerField(default=0,null=True,blank=True)
    date_of_join = models.DateTimeField(auto_now_add=True)

    user_choices = (
        ('stud','Student'),
        ('T-S','Teaching-Staff'),
        ('NT-S','NonTeaching-Staff'),
    )
    
    user_type = models.CharField(max_length=10,choices=user_choices,default='stud')
    nationality = models.CharField(max_length=50,blank=True,null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

class Student(SchoolBaseModel):
    student = models.OneToOneField(User,related_name='student_name',on_delete=models.CASCADE)
    roll_num = models.CharField(max_length=10,unique=True)
    academic_year = models.CharField(max_length=30)
    class_details = models.ForeignKey('Class_Details',related_name='student_class',on_delete=models.CASCADE,null=True,blank=True)
    school = models.ForeignKey('School',related_name='students_school',on_delete=models.CASCADE)

    def __str__(self):
        return self.roll_num

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'

class Standard(SchoolBaseModel):
    standard_name = models.IntegerField(validators=[MaxValueValidator(12)],unique=True)
    
    def __str__(self):
        return f'{self.standard_name}'

    class Meta:
        verbose_name = 'standard'
        verbose_name_plural = 'standards'

class Section(SchoolBaseModel):
    section_name = models.CharField(max_length=5,unique=True)

    def __str__(self):
        return self.section_name

    class Meta:
        verbose_name = 'section'
        verbose_name_plural = 'sections'


class Major(SchoolBaseModel):
    parent = models.ForeignKey('self',blank=True,null=True,related_name='child',on_delete=models.CASCADE)
    title = models.CharField(max_length=40,unique = True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'major'
        verbose_name_plural = 'majors'

class Class_Details(SchoolBaseModel):
    standard = models.ForeignKey(Standard,related_name='class_standard',on_delete=models.CASCADE)
    section = models.ForeignKey(Section,related_name='class_section',on_delete=models.CASCADE)
    major = models.ForeignKey(Major,related_name='class_major',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f'{self.standard.standard_name} - {self.section.section_name}'

    class Meta:
        verbose_name = 'Class_Detail'
        verbose_name_plural = 'Class_Details'

class School(SchoolBaseModel):
    school_name = models.CharField(max_length=75)
    founder = models.CharField(max_length=30)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.school_name

    class Meta:
        verbose_name = 'school'
        verbose_name_plural = 'schools'

class Staff(SchoolBaseModel):
    staff = models.ForeignKey(User,related_name='staff_name',on_delete=models.CASCADE)
    designation = models.CharField(max_length=50)
    school = models.ForeignKey(School,related_name='staff_school',on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.staff.username} - {self.designation}'

    class Meta:
        verbose_name = 'staff'
        verbose_name_plural = 'staffs'


class Teaching_Staff_Details(SchoolBaseModel):
    staff_name = models.ForeignKey(Staff,related_name='staff_detail',on_delete=models.CASCADE)
    class_detail = models.ForeignKey(Class_Details,related_name='staff_class',on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject',related_name='staff_subject',on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return f'{self.staff_name.staff.username} - {self.class_detail}'
    
    class Meta:
        verbose_name = 'staff-detail'
        verbose_name_plural = 'staff-details'


class Subject(SchoolBaseModel):
    title = models.CharField(max_length=30)
    subject_major = models.ForeignKey(Major,related_name='subjects',on_delete=models.CASCADE) 

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'subject'
        verbose_name_plural = 'subjects'


class Exam(SchoolBaseModel):
    category = models.ForeignKey('Exam_Category',related_name='exams',on_delete=models.CASCADE)
    total = models.IntegerField(default=500)
    start_date = models.DateField()
    end_date = models.DateField()
    school = models.ForeignKey(School,related_name='exams',on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category.category_name} - {self.school.school_name}'

    class Meta:
        verbose_name = 'exam'
        verbose_name_plural = 'exams'


class Exam_Category(SchoolBaseModel):
    parent_id = models.ForeignKey('self',related_name='child',on_delete=models.CASCADE,blank=True,null=True)
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name
    
    class Meta:
        verbose_name = 'exam_category'
        verbose_name_plural = 'exam_categories'


class Result(SchoolBaseModel):
    exam_name = models.ForeignKey(Exam,related_name='exam_results',on_delete=models.CASCADE)
    student_name = models.ForeignKey(Student,related_name='student_results',on_delete=models.CASCADE)
    subject_name = models.ForeignKey(Subject,related_name='subject_results',on_delete=models.CASCADE)

    marks = models.FloatField(default=1,validators=[MaxValueValidator(100),MinValueValidator(0)])
    grade = models.CharField(max_length=15,blank=True,null=True)

    result_status = models.CharField(max_length=10,default='pass',blank=True,null=True)

    def save(self,*args, **kwargs):
        if self.marks>90:
            self.grade = 'O'
        elif self.marks in range(75,90):
            self.grade = 'A'
        elif self.marks in range(60,75):
            self.grade = 'B'
        elif self.marks in range(50,60):
            self.grade = 'C'
        elif self.grade in range(35,50):
            self.grade = 'E'
        else:
            self.grade = 'D'
        
        if self.marks in range(35,100):
            self.result_status = 'Pass'
        else:
            self.result_status = 'Fail'
        
        super(Result,self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.student_name}-{self.exam_name}-{self.subject_name}'
    
    class Meta:
        verbose_name = 'result'
        verbose_name_plural = 'results'



            
        
