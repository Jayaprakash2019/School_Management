from django.contrib import admin
from .models import Attendance,Class,ClassMember,Exam,Marks,Subject,User

# Register your models here.

admin.site.register(User)
admin.site.register(Attendance)
admin.site.register(Class)
admin.site.register(ClassMember)
admin.site.register(Exam)
admin.site.register(Marks)
admin.site.register(Subject)
