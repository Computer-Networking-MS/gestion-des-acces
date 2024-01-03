from django.contrib import admin
from .models import Faculty, Department, Branch, Student, Course, Session, Exam, StudentOfSession
# Register your models here.
admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(Branch)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Session)
admin.site.register(Exam)
admin.site.register(StudentOfSession)