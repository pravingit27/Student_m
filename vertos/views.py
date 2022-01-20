from datetime import datetime

from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import request, status
from rest_framework import generics
from rest_framework.authtoken.models import Token

from .models import *
from .serializers import *
from .permissions import *
from .exceptions import *

# Create your views here.
class UserView(generics.ListCreateAPIView):
    #queryset = User.objects.filter(status = True, deleted = False).order_by('pk')
    serializer_class = UserSerializer
    permission_classes = (IsUser,)

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user,status = True,deleted = False)

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            queryset = User.objects.filter(status = True, deleted = False).order_by('pk')
            return queryset
        else: 
            queryset = User.objects.filter(pk = self.request.user.pk)
            if queryset.exists():
                return queryset
            else:
                raise NonUser()

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(status = True,deleted = False).order_by('pk')
    serializer_class = UserSerializer
    permission_classes = (IsUser,)

    def perform_update(self, serializer):
        serializer.save(updated_by = self.request.user, updated_at = datetime.now())

    def retrieve(self, request, *args, **kwargs):
        url_pk = self.kwargs['pk']
        if url_pk == self.request.user.pk or self.request.user.is_staff or self.request.user.is_superuser:
            try:
                queryset = User.objects.get(pk = url_pk)
                return Response(UserSerializer(queryset).data)
            except User.DoesNotExist:
                return Response({"message": "you are not a user"})
        else:
            return Response({"message":"You can't view other user details"})
 
    def destroy(self, request, *args, **kwargs):
        s = self.get_object()
        s.status = False
        s.deleted = True
        s.deleted_by = self.request.user
        s.deleted_at = datetime.now()
        s.save()
        return Response({"message":"The Data Has Been Deleted Successfully"})

class StudentView(generics.ListCreateAPIView):
    #queryset = Student.objects.filter(status=True, deleted=False).order_by('pk')
    serializer_class = StudentSerializer
    permission_classes = (IsStudent,)
    
    def perform_create(self, serializer):
        if self.request.user.is_staff or self.request.user.is_superuser:
            serializer.save(created_by = self.request.user,status = True,deleted = False)
        else:
            raise NonStudent()

    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            queryset = Student.objects.filter(status = True, deleted = False).order_by('pk')
            return queryset
        else: 
            queryset = Student.objects.filter(student__username = self.request.user.username)
            if queryset.exists():
                return queryset
            else:
                raise NonStudent()

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.filter(status=True, deleted=False).order_by('pk')
    serializer_class = StudentSerializer
    permission_classes = (IsStudent,)

    def perform_update(self, serializer):
        url_pk = self.kwargs['pk']
        if url_pk == self.request.user.pk or self.request.user.is_staff or self.request.user.is_superuser:
            serializer.save(updated_by = self.request.user)

    def retrieve(self, request, *args, **kwargs):
        url_pk = self.kwargs['pk']
        if url_pk == self.request.user.pk or self.request.user.is_staff or self.request.user.is_superuser:
            try:
                queryset = Student.objects.get(pk = url_pk)
                return Response(StudentSerializer(queryset).data)
            except Student.DoesNotExist:
                return Response({"message": "you are not a Student or a Staff To View Student Details"})
        else:
            return Response({"message":"You can't view other Student details"})
    
    def destroy(self, request, *args, **kwargs):
        url_pk = self.kwargs['pk']
        if url_pk == self.request.user.pk or self.request.user.is_staff or self.request.user.is_superuser:
            print(self.get_object())
            s = self.get_object()
            s.status = False
            s.deleted = True
            s.deleted_by = self.request.user
            s.deleted_at = timezone.now()
            s.save()
            return Response({"message": "The Data Has Been Deleted"})
    
class StandardView(generics.ListCreateAPIView):
    queryset = Standard.objects.filter(status=True, deleted=False).order_by('pk')
    serializer_class = StandardSerializer
     
    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)

class StandardDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Standard.objects.filter(status=True, deleted=False).order_by('pk')
    serializer_class = StandardSerializer
    permission_classes = (IsTeachingStaff,)
    
    def perform_update(self, serializer):
        serializer.save(updated_by = self.request.user)
    
    def destroy(self, request, *args, **kwargs):
        print(self.get_object())
        s = self.get_object()
        s.status = False
        s.deleted = True
        s.deleted_by = self.request.user
        s.deleted_at = timezone.now()
        s.save()
        return Response(StandardSerializer(self.get_object()).data)

class SectionView(generics.ListCreateAPIView):
    queryset = Section.objects.filter(status=True, deleted=False).order_by('pk')
    serializer_class = SectionSerializer
     
    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)

class SectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Section.objects.filter(status=True, deleted=False).order_by('pk')
    serializer_class = SectionSerializer

    def perform_update(self, serializer):
        serializer.save(updated_by = self.request.user)
    
    def destroy(self, request, *args, **kwargs):
        #print(self.get_object())
        s = self.get_object()
        s.status = False
        s.deleted = True
        s.deleted_by = self.request.user
        s.deleted_at = timezone.now()
        s.save()
        return Response(SectionSerializer(self.get_object()).data)

class MajorView(generics.ListCreateAPIView):
    queryset = Major.objects.filter(status=True, deleted=False).order_by('pk')
    serializer_class = MajorSerializer

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)

class MajorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Major.objects.filter(status=True, deleted=False).order_by('pk')
    serializer_class = MajorSerializer
    permission_classes = (IsTeachingStaff,)

    def perform_update(self, serializer):
        serializer.save(updated_by = self.request.user)

    def destroy(self, request, *args, **kwargs):
        #print(self.get_object())
        s = self.get_object()
        s.status = False
        s.deleted = True
        s.deleted_by = self.request.user
        s.deleted_at = timezone.now()
        s.save()
        return Response(MajorSerializer(self.get_object()).data)

class ClassView(generics.ListCreateAPIView):
    queryset = Class_Details.objects.filter(status=True, deleted=False).order_by('pk')
    serializer_class = ClassDetailSerializer
    
    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)

class ClassDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Class_Details.objects.filter(status=True, deleted=False).order_by('pk')
    serializer_class = ClassDetailSerializer
    permission_classes = (IsTeachingStaff,)

    def perform_update(self, serializer):
        serializer.save(updated_by = self.request.user)

    def destroy(self, request, *args, **kwargs):
        #print(self.get_object())
        s = self.get_object()
        s.status = False
        s.deleted = True
        s.deleted_by = self.request.user
        s.deleted_at = timezone.now()
        s.save()
        return Response(ClassDetailSerializer(self.get_object()).data)

class StaffView(generics.ListCreateAPIView):
    #queryset = Staff.objects.filter(status=True, deleted=False).order_by('pk')
    serializer_class = StaffSerializers
    permission_classes = (IsStaff,)

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user,status = True,deleted = False)
    
    def get_queryset(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            queryset = Staff.objects.filter(status = True, deleted = False).order_by('pk')
            return queryset
        else: 
            queryset = Staff.objects.filter(staff__username = self.request.user.username)
            if queryset.exists():
                return queryset
            else:
                raise UnAuthorizedPerson()
           
class StaffDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.filter(status=True, deleted=False).order_by('pk')
    serializer_class = StaffSerializers
    permission_classes = (IsStaff,)

    def perform_update(self, serializer):
        url_pk = self.kwargs['pk']
        if url_pk == self.request.user.pk or self.request.user.is_staff or self.request.user.is_superuser:
            serializer.save(updated_by = self.request.user)

    def retrieve(self, request, *args, **kwargs):
        url_pk = self.kwargs['pk']
        if url_pk == self.request.user.pk or self.request.user.is_staff or self.request.user.is_superuser:
            try:
                queryset = Staff.objects.get(staff__pk = url_pk)
                return Response(StaffSerializers(queryset).data)
            except Staff.DoesNotExist:
                raise NonStaff()
        else:
            return Response({"message":"You can't view other staff details"})

    def destroy(self, request, *args, **kwargs):
        url_pk = self.kwargs['pk']
        #print(self.get_object())
        if url_pk == self.request.user.pk or self.request.user.is_staff or self.request.user.is_superuser:
            s = self.get_object()
            s.status = False
            s.deleted = True
            s.deleted_by = self.request.user
            s.deleted_at = timezone.now()
            s.save()
            return Response({"message":"The Data Has Been Deleted"})
    
class TeachingStaffView(generics.ListCreateAPIView):
    queryset = Teaching_Staff_Details.objects.filter(status=True, deleted=False).order_by('pk')
    serializer_class = TeachingStaffSerializers
    permission_classes = (IsTeachingStaff,)
    
    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user,status = True,deleted = False)

class TeachingStaffDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teaching_Staff_Details.objects.filter(status=True, deleted=False).order_by('pk')
    serializer_class = TeachingStaffSerializers
    permission_classes = (IsTeachingStaff,)

    def perform_update(self, serializer):
        serializer.save(updated_by = self.request.user)
    
    def destroy(self, request, *args, **kwargs):
        #print(self.get_object())
        s = self.get_object()
        s.status = False
        s.deleted = True
        s.deleted_by = self.request.user
        s.deleted_at = timezone.now()
        s.save()
        return Response({"message":"The Data Has Been Deleted"})

class SubjectView(generics.ListCreateAPIView):
    queryset = Subject.objects.filter(status=True, deleted=False).order_by('pk')
    serializer_class = SubjectSerializers

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user,status = True,deleted = False)

class SubjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.filter(status=True, deleted=False).order_by('pk')
    serializer_class = SubjectSerializers
    permission_classes = (IsTeachingStaff,)

    def perform_update(self, serializer):
        serializer.save(updated_by = self.request.user)

    def destroy(self, request, *args, **kwargs):
        #print(self.get_object())
        s = self.get_object()
        s.status = False
        s.deleted = True
        s.deleted_by = self.request.user
        s.deleted_at = timezone.now()
        s.save()
        return Response({"message":"The Data Has Been Deleted"})

class ExamCategoryView(generics.ListCreateAPIView):
    queryset = Exam_Category.objects.filter(status=True, deleted=False).order_by('pk')
    serializer_class = ExamCategorySerializer
    permission_classes = (IsAdmin,)

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)

class ExamCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exam_Category.objects.filter(status=True, deleted=False).order_by('pk')
    serializer_class = ExamCategorySerializer
    permission_classes = (IsAdmin,)

    def perform_update(self, serializer):
        serializer.save(updated_by = self.request.user,status = True,deleted = False)
    
    def destroy(self, request, *args, **kwargs):
        #print(self.get_object())
        s = self.get_object()
        s.status = False
        s.deleted = True
        s.deleted_by = self.request.user
        s.deleted_at = timezone.now()
        s.save()
        return Response({"message":"The Data Has Been Deleted"})

class ExamView(generics.ListCreateAPIView):
    queryset = Exam.objects.filter(status=True, deleted=False).order_by('pk')
    serializer_class = ExamSerializers
    permission_classes = (IsAdmin,)

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user,status = True,deleted = False)

class ExamDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exam.objects.filter(status=True, deleted=False).order_by('pk')
    serializer_class = ExamSerializers
    permission_classes = (IsAdmin,)

    def perform_update(self, serializer):
        serializer.save(updated_by = self.request.user)
    
    def destroy(self, request, *args, **kwargs):
        #print(self.get_object())
        s = self.get_object()
        s.status = False
        s.deleted = True
        s.deleted_by = self.request.user
        s.deleted_at = timezone.now()
        s.save()
        return Response({"message":"The Data Has Been Deleted"})
    
class ResultView(generics.ListCreateAPIView):
    queryset = Result.objects.filter(status=True, deleted=False).order_by('pk')
    serializer_class = ResultSerializer
    permission_classes = (IsAdmin,)

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user,status = True,deleted = False)

class ResultDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Result.objects.filter(status=True, deleted=False).order_by('pk')
    serializer_class = ResultSerializer
    permission_classes = (IsAdmin,)

    def perform_update(self, serializer):
        serializer.save(updated_by = self.request.user)
    
    def destroy(self, request, *args, **kwargs):
        #print(self.get_object())
        s = self.get_object()
        s.status = False
        s.deleted = True
        s.deleted_by = self.request.user
        s.deleted_at = timezone.now()
        s.save()
        return Response({"message":"The Data Has Been Deleted"})

class SchoolView(generics.ListCreateAPIView):
    queryset = School.objects.filter(status=True,deleted = False).order_by('pk')
    serializer_class = SchoolSerializer
    permission_classes = (IsAdmin,)

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user,status = True,deleted = False)

class SchoolDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.filter(status=True,deleted=False).order_by('pk')
    serializer_class = SchoolSerializer
    permission_classes = (IsAdmin,)

    def perform_update(self, serializer):
        serializer.save(updated_by = self.request.user)

    def destroy(self, request, *args, **kwargs):
        #print(self.get_object())
        s = self.get_object()
        s.status = False
        s.deleted = True
        s.deleted_by = self.request.user
        s.deleted_at = timezone.now()
        s.save()
        return Response({"message":"The Data Has Been Deleted"})

class LogoutView(APIView):
    def post(self,request):
        Token.objects.get(user = request.user).delete()
        return Response({"Success": "Logout has been Successfull"},status = status.HTTP_200_OK)

@receiver(post_save,sender = User)
def create_token_user(sender,instance = None,created = False,**kwargs):
    if created:
        Token.objects.create(user = instance)

