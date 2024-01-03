from django.db import models


# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', '-created']
        
    def __str__(self) -> str:
        
        return self.name


class Department(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', '-created']
        
    def __str__(self) -> str:
        return self.name

class Branch(models.Model):     
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', '-created']
        
    def __str__(self) -> str:
        return self.name

class Student(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    matricule = models.CharField(max_length=200,default='')
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    dateOfBirth = models.DateField(auto_now=False, auto_now_add=False)
    image = models.ImageField(upload_to="student_pic", height_field=None, width_field=None, max_length=100)
    imageDataSet = models.CharField(max_length=100,default="")
    paymentStatus1 = models.CharField(max_length=100)
    paymentStatus2 = models.CharField(max_length=100)
    admitted = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self) -> str:
        return self.name

    

class Course(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering  = ['-updated', '-created']
        
    def __str__(self) -> str:
        return self.name
      
    
class Session(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    begin_at = models.DateField(auto_now=False, auto_now_add=False)
    end_at = models.DateField(auto_now=False, auto_now_add=False)
    participants = models.ManyToManyField(Student, related_name="participants", blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', '-created']
        
    def __str__(self) -> str:
        return self.name 

class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    examDate = models.DateField(auto_now=False, auto_now_add=False)
    begin_at = models.TimeField(auto_now=False, auto_now_add=False)
    end_at = models.TimeField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', '-created']
        
    def __str__(self) -> str:
        return self.name 

class StudentOfSession(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    level = models.IntegerField()
    status = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-updated', '-created']
        
    def __str__(self) -> str:
        return self.name 