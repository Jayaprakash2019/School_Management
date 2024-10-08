from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import UserSerializer,ClassSerializer,AttendanceSerializer,SubjectSerializer,ExamSerializer,MarksSerializer
from django.shortcuts import get_object_or_404
from .models import Class,Attendance,Subject

User = get_user_model()
class UserList(APIView):
    def get(self, request):
        users = User.objects.all()  # Non-deleted users
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    def get(self, request, id):
        user = get_object_or_404(User.objects_with_deleted, pk=id)  # Include soft-deleted users
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, id):
        user = get_object_or_404(User.objects_with_deleted, pk=id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        user = get_object_or_404(User.objects_with_deleted, pk=id)
        user.delete()  # Soft delete
        return Response(status=status.HTTP_204_NO_CONTENT)

#classes
class ClassList(APIView):
    def get(self, request):
        classes = Class.objects.all()  # Non-deleted classes
        serializer = ClassSerializer(classes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClassDetail(APIView):
    def get(self, request, id):
        class_instance = get_object_or_404(Class.objects_with_deleted, pk=id)  # Include soft-deleted classes
        serializer = ClassSerializer(class_instance)
        return Response(serializer.data)

    def put(self, request, id):
        class_instance = get_object_or_404(Class.objects_with_deleted, pk=id)
        serializer = ClassSerializer(class_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        class_instance = get_object_or_404(Class.objects_with_deleted, pk=id)
        class_instance.delete()  # Soft delete
        return Response(status=status.HTTP_204_NO_CONTENT)


#classMember

#Attendance
class AttendanceList(APIView):
    def get(self, request):
        attendance = Attendance.objects.all()  # Non-deleted attendance records
        serializer = AttendanceSerializer(attendance, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AttendanceDetail(APIView):
    def get(self, request, id):
        attendance = get_object_or_404(Attendance.objects_with_deleted, pk=id)  # Include soft-deleted records
        serializer = AttendanceSerializer(attendance)
        return Response(serializer.data)

    def put(self, request, id):
        attendance = get_object_or_404(Attendance.objects_with_deleted, pk=id)
        serializer = AttendanceSerializer(attendance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        attendance = get_object_or_404(Attendance.objects_with_deleted, pk=id)
        attendance.delete()  # Soft delete
        return Response(status=status.HTTP_204_NO_CONTENT)

#subject
class SubjectList(APIView):
    def get(self, request):
        subjects = Subject.objects.all()  # Non-deleted subjects
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SubjectDetail(APIView):
    def get(self, request, id):
        subject = get_object_or_404(Subject.objects_with_deleted, pk=id)  # Include soft-deleted subjects
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)

    def put(self, request, id):
        subject = get_object_or_404(Subject.objects_with_deleted, pk=id)
        serializer = SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        subject = get_object_or_404(Subject.objects_with_deleted, pk=id)
        subject.delete()  # Soft delete
        return Response(status=status.HTTP_204_NO_CONTENT)

#Exam
class ExamList(APIView):
    def get(self, request):
        exams = Exam.objects.all()  # Non-deleted exams
        serializer = ExamSerializer(exams, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ExamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExamDetail(APIView):
    def get(self, request, id):
        exam = get_object_or_404(Exam.objects_with_deleted, pk=id)  # Include soft-deleted exams
        serializer = ExamSerializer(exam)
        return Response(serializer.data)

    def put(self, request, id):
        exam = get_object_or_404(Exam.objects_with_deleted, pk=id)
        serializer = ExamSerializer(exam, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        exam = get_object_or_404(Exam.objects_with_deleted, pk=id)
        exam.delete()  # Soft delete
        return Response(status=status.HTTP_204_NO_CONTENT)

#Marks
class MarksList(APIView):
    def get(self, request):
        marks = Marks.objects.all()  # Non-deleted marks
        serializer = MarksSerializer(marks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MarksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MarksDetail(APIView):
    def get(self, request, id):
        marks = get_object_or_404(Marks.objects_with_deleted, pk=id)  # Include soft-deleted marks
        serializer = MarksSerializer(marks)
        return Response(serializer.data)

    def put(self, request, id):
        marks = get_object_or_404(Marks.objects_with_deleted, pk=id)
        serializer = MarksSerializer(marks, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        marks = get_object_or_404(Marks.objects_with_deleted, pk=id)
        marks.delete()  # Soft delete
        return Response(status=status.HTTP_204_NO_CONTENT)
