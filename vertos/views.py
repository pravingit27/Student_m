from rest_framework import generics
from rest_framework import permissions
from datetime import datetime
from django.utils import timezone

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import *
from .serializers import *
from .permissions import *

# Create your views here.
class UserView(generics.ListCreateAPIView):
    queryset = User.objects.filter(status = True, deleted = False).order_by('pk')
    serializer_class = UserSerializer
    #permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter(status = True,deleted = False).order_by('pk')
    serializer_class = UserSerializer
    #permission_classes = (IsAuthenticated,)

    def perform_update(self, serializer):
        serializer.save(updated_by = self.request.user, updated_at = datetime.now())
    
    def destroy(self, request, *args, **kwargs):
        s = self.get_object()
        s.status = False
        s.deleted = True
        s.deleted_by = self.request.user
        s.deleted_at = datetime.now()
        s.save()
        return Response(UserSerializer(self.get_object()).data)

class StudentView(generics.ListCreateAPIView):
    queryset = Student.objects.filter(status=True, deleted=False).order_by('pk')
    serializer_class = StudentSerializer
    permission_classes = (IsStudent,)
    
    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.filter(status=True, deleted=False).order_by('pk')
    serializer_class = StudentSerializer
    permission_classes = (IsStudent,)

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
        return Response(StudentSerializer(self.get_object()).data)
    
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
    queryset = Staff.objects.filter(status=True, deleted=False).order_by('pk')
    serializer_class = StaffSerializers
    permission_classes = (IsStaff,)

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)

class StaffDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.filter(status=True, deleted=False).order_by('pk')
    serializer_class = StaffSerializers
    permission_classes = (IsStaff,)

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
        return Response(StaffSerializers(self.get_object()).data)
    
class TeachingStaffView(generics.ListCreateAPIView):
    queryset = Teaching_Staff_Details.objects.filter(status=True, deleted=False).order_by('pk')
    serializer_class = TeachingStaffSerializers
    
    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)

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
        return Response(TeachingStaffSerializers(self.get_object()).data)

class SubjectView(generics.ListCreateAPIView):
    queryset = Subject.objects.filter(status=True, deleted=False).order_by('pk')
    serializer_class = SubjectSerializers

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)

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
        return Response(SubjectSerializers(self.get_object()).data)

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
        serializer.save(updated_by = self.request.user)
    
    def destroy(self, request, *args, **kwargs):
        #print(self.get_object())
        s = self.get_object()
        s.status = False
        s.deleted = True
        s.deleted_by = self.request.user
        s.deleted_at = timezone.now()
        s.save()
        return Response(ExamCategorySerializer(self.get_object()).data)

class ExamView(generics.ListCreateAPIView):
    queryset = Exam.objects.filter(status=True, deleted=False).order_by('pk')
    serializer_class = ExamSerializers
    permission_classes = (IsAdmin,)

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)

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
        return Response(ExamSerializers(self.get_object()).data)
    
class ResultView(generics.ListCreateAPIView):
    queryset = Result.objects.filter(status=True, deleted=False).order_by('pk')
    serializer_class = ResultSerializer
    permission_classes = (IsAdmin,)

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)

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
        return Response(ResultSerializer(self.get_object()).data)

class SchoolView(generics.ListCreateAPIView):
    queryset = School.objects.filter(status=True,deleted = False).order_by('pk')
    serializer_class = SchoolSerializer
    permission_classes = (IsAdmin,)

    def perform_create(self, serializer):
        serializer.save(created_by = self.request.user)

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
        return Response(SchoolSerializer(self.get_object()).data)

class Logout(APIView):
    def get(self,request):
        request.user.auth_token.delete()
        return Response({"Success": "Logout has been Successfull"},status = status.HTTP_200_OK)

