from rest_framework.exceptions import APIException


class UnAuthorizedPerson(APIException):
    status_code = 400
    default_detail = "You are not authorized to view Staff"
    default_code = "You are not authorized to view Staff"

class NonStaff(APIException):
    status_code = 400
    default_detail = "You are not a Staff"
    default_code = "You are not a Staff"

class NonStudent(APIException):
    status_code = 400
    default_detail = "You are not a student or a Staff"
    default_code = "You are not a Student or a Staff"

class NoStudent(APIException):
    status_code = 400
    default_detail = "Student Detail is not exists"
    default_code = "Student Detail is not exists"

class NonUser(APIException):
    status_code = 400
    default_detail = "You are not a User"
    default_code = "You are not a User"

class NoTeacher(APIException):
    status_code = 400
    default_detail = "The Teacher details are not exists"
    default_code = "The Teacher details are not exists"

class NoStaff(APIException):
    status_code = 400
    default_detail = "The Staff details is not exists"
    default_code = "The Staff details is not exists"