from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager


class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    def hard_delete(self, *args, **kwargs):
        """ Completely deletes the object from the database """
        super(SoftDeleteModel, self).delete(*args, **kwargs)

    class Meta:
        abstract = True

class SoftDeleteManager(BaseUserManager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)

# Custom User model
class User(AbstractUser, SoftDeleteModel):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('admin', 'Admin'),
    ]
    
    # Custom fields
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    email = models.EmailField(unique=True)

    objects = SoftDeleteManager()  # Use the soft delete manager
    
    def __str__(self):
        return self.username
    
#class
class Class(SoftDeleteModel):
    class_name = models.CharField(max_length=255)
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='classes')

    objects = SoftDeleteManager()

    def __str__(self):
        return self.class_name

# ClassMember model
class ClassMember(SoftDeleteModel):
    fk_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='members')
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='class_memberships')

    objects = SoftDeleteManager()

    def __str__(self):
        return f"{self.fk_user} in {self.fk_class}"


# Attendance model
class Attendance(SoftDeleteModel):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
    ]
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='attendance_records')
    fk_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='attendance_records')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    date = models.DateField()

    objects = SoftDeleteManager()

    def __str__(self):
        return f"{self.fk_user} - {self.status} on {self.date}"

# Subject model
class Subject(SoftDeleteModel):
    subject_name = models.CharField(max_length=255)
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    objects = SoftDeleteManager()

    def __str__(self):
        return self.subject_name

# Exam model
class Exam(SoftDeleteModel):
    exam_name = models.CharField(max_length=255)
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date = models.DateField()

    objects = SoftDeleteManager()

    def __str__(self):
        return self.exam_name

# Marks model
class Marks(SoftDeleteModel):
    fk_subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='marks')
    fk_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='marks')
    fk_exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='marks')
    mark = models.FloatField()

    objects = SoftDeleteManager()

    def __str__(self):
        return f"{self.fk_user} - {self.mark} in {self.fk_subject} for {self.fk_exam}"

