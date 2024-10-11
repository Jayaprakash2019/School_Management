from rest_framework.permissions import BasePermission

class IsAuthenticatedAndRole(BasePermission):
    """
    Base permission to check if the user is authenticated and has the required role.
    """
    required_role = None

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == self.required_role)


class IsAdmin(IsAuthenticatedAndRole):
    """
    Permission class for admin users.
    """
    required_role = 'admin'


class IsTeacher(IsAuthenticatedAndRole):
    """
    Permission class for teacher users.
    """
    required_role = 'teacher'


class IsStudent(IsAuthenticatedAndRole):
    """
    Permission class for student users.
    """
    required_role = 'student'


class IsAdminOrTeacher(BasePermission):
    """
    Custom permission to allow access to users with either the 'admin' or 'teacher' role.
    """
    def has_permission(self, request, view):
        return bool(
            request.user and 
            request.user.is_authenticated and 
            (request.user.role == 'admin' or request.user.role == 'teacher')
        )

class IsAdminOrTeacherOrStudent(BasePermission):
    """
    Custom permission to allow access to users with either the 'admin' or 'teacher' role.
    """
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            (request.user.role == 'admin' or request.user.role == 'teacher' or request.user.role == 'student')
        )
        