from django.db.models import fields
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from rest_framework.compat import distinct
from vertos.models import *
from rest_framework import serializers

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

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ('created_by','updated_by','deleted_by','status','deleted',)

    def to_representation(self, instance):
        #print(instance.school)
        return{
            "id": instance.pk,
            "student_name": instance.student.username,
            "roll_num" : instance.roll_num,
            "academic_year" : instance.academic_year,
            "class_details":f'{instance.class_details.standard}-{instance.class_details.section}',
            "school": SchoolSerializer(instance.school).data,
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





