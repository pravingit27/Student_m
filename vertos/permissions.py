from rest_framework.permissions import IsAuthenticated
from .models import *

class IsStudent(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user and request.user.user_type == 'stud' or 'T-S' 

class IsStaff(IsAuthenticated):
    def has_permission(self, request,view):
        print(request.user.user_type)
        return request.user.is_authenticated and request.user and request.user.user_type != 'stud'
       
class IsTeachingStaff(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user and request.user.user_type == 'T-S'

class IsAdmin(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user and request.user.is_staff

class IsUser(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user 
    