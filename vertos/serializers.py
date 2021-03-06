from django.db.models import Sum
from django.forms import fields
from vertos.models import *
from rest_framework import serializers
from django.db.models import Q

class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolBaseModel

        fields = '__all__'

    def to_representation(self, instance):
        return {
            "status" : instance.status,
            "deleted" : instance.deleted,
            "created_by" : instance.username,
            "updated_by" : instance.username,
        }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('is_superuser','last_login','groups','created_by','updated_by','deleted_by','status','deleted',)

    def to_representation(self,instance):
        return{
            "id" : instance.pk,
            "username":instance.username,
            "email":instance.email,
            "first_name":instance.first_name,
            "last_name":instance.last_name,
            "gender":instance.gender,
            "phone_num":instance.phone_num,
            "age":instance.age,
            "date_of_joined":instance.date_of_join,
            "role":instance.user_type,
            "nationality":instance.nationality,
            "created_by" : instance.username,
            "updated_by" : instance.username,
            "is_staff" : instance.is_staff,
            }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def update(self, instance, validated_data):
        for k,v in validated_data.items():
            if k == 'password':
                instance.set_password(v)
            else:
                setattr(instance,k,v)
            instance.save()
            return instance

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School

        #fields = '__all__'
        exclude = ('created_by','updated_by','deleted_by','status','deleted')

    def to_representation(self, instance):
        return {
            "id" : instance.pk,
            "school" : instance.school_name,
            "address" : instance.address,
        }

class StudentSerializer(serializers.Serializer):
    class Meta:
        model = Student
        exclude = ('created_by','updated_by','deleted_by','status','deleted','total_marks')

    def to_representation(self, instance):
        #print(instance.school)
        return{
            "id": instance.pk,
            "student_name": instance.student.username,
            "roll_num" : instance.roll_num if instance.roll_num else None,
            "academic_year" : instance.academic_year if instance.academic_year else None,
            "class_details": f'{instance.class_details.standard}-{instance.class_details.section}' if instance.class_details else None,
            "school": SchoolSerializer(instance.school).data if instance.school else None,
            "total_marks" : instance.total_marks if instance.total_marks else None,
        }

class StandardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Standard

        fields = '__all__'

    def to_representation(self, instance):
        return {
            "id" : instance.pk,
            "class" : instance.standard_name,
        }

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section

        fields = '__all__'

    def to_representation(self, instance):
        return {
            "id" : instance.pk,
            "section" : instance.section_name,
        }

class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major

        fields = '__all__'
    
    def to_representation(self, instance):
        return {
            "id" : instance.pk,
            "major" : instance.title,
            "parent_title" : f'{instance.parent}'
        }

class ClassDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class_Details

        fields = '__all__'

    def to_representation(self, instance):
        return {
            "id" : instance.pk,
            "standard" : instance.standard.standard_name,
            "section" : instance.section.section_name,
            "major" : instance.major.title,
        }

class StaffSerializers(serializers.ModelSerializer):
    class Meta:
        model = Staff

        exclude = ('created_by','updated_by','deleted_by','status','deleted',)
    
    def __init__(self,*args, **kwargs):
        super(StaffSerializers,self).__init__(*args, **kwargs)
        self.fields['staff'].queryset = User.objects.filter(Q(user_type = 'T-S')|Q(user_type = 'NT-S'))

    def to_representation(self, instance):
        return {
            "id" : instance.pk,
            "staff" : instance.staff.username,
            "designation" : instance.designation,
            "school" : instance.school.school_name,
        }

class TeachingStaffSerializers(serializers.ModelSerializer):
    class Meta:
        model = Teaching_Staff_Details

        exclude = ('created_by','updated_by','deleted_by','status','deleted',)

    def to_representation(self, instance):
        return {
            "id" : instance.pk,
            "staff" : StaffSerializers(instance.staff_name).data,
            "class" : ClassDetailSerializer(instance.class_detail).data,
            "subject" : instance.subject.title,
        }

class SubjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subject

        exclude = ('created_by','updated_by','deleted_by','status','deleted',)

    def to_representation(self, instance):
        return {
            "id": instance.pk,
            "subject" : instance.title,
            "major" : instance.subject_major.title,
        }

class ExamCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam_Category

        exclude = ('created_by','updated_by','deleted_by','status','deleted',)
    
    def to_representation(self, instance):
        return {
            "id" : instance.pk,
            "Exam_Type" : instance.category_name,
            "parent_category" : f'{instance.parent_id}',
        }

class ExamSerializers(serializers.ModelSerializer):
    class Meta:
        model = Exam

        exclude = ('created_by','updated_by','deleted_by','status','deleted',)

    def to_representation(self, instance):
        return {
            "id" : instance.pk,
            "category" : ExamCategorySerializer(instance.category).data,
            "total_marks" : instance.total,
            "starting_date" : instance.start_date,
            "ending_date" : instance.end_date,
            "school" : instance.school.school_name, 
        }
        
class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        exclude = ('grade','result_status','created_by','updated_by','deleted_by','status','deleted',)

    def to_representation(self, instance):
        return {
            "id" : instance.pk,
            "exam_name" : instance.exam_name.category.category_name,
            "subject_name" : instance.subject_name.title,
            "student_name" : StudentSerializer(instance.student_name).data,
            "marks" : instance.marks,
            "grade" : instance.grade,
            "result_status" : instance.result_status,
        } 

class RankSerializer(serializers.Serializer):
    fields = ('id','total_marks','student_name')

    def to_representation(self, instance):
        total_marks = Student.objects.annotate(total = Sum('student_results__marks'))
        return {
            "id" : instance.pk,
            "total_marks" : instance.total_marks,
            "student_name" : instance.student_name,
        }






