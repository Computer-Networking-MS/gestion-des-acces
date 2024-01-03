from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import StudentRegistrationForm
from .models import Student
from .utils import \
    create_dataset  # Assuming you have a function for creating datasets
from datetime import datetime

# Create your views here.
def home(request):
    return render(request, 'base.html')

# views.py
def generate_matricule(student):
    # Extract month, day, and year from the created_at attribute
    created_at = student.created
    month = str(created_at.month).zfill(2)  # Zero-padding for single-digit months
    day = str(created_at.day).zfill(2)  # Zero-padding for single-digit days
    year = str(created_at.year)[2:]  # Use the last two digits of the year

    # Extract the first letter of the faculty's name
    faculty_first_letter = student.branch.faculty.name[0].upper()

    # Extract the student ID from the database (assuming it's an integer)
    student_id = str(student.id).zfill(4)  # Assuming a 4-digit student ID

    # Concatenate the components to form the matricule
    matricule = f"{month}{day}{year}{faculty_first_letter}{student_id}"

    return matricule

def student_registration(request):
    
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            # Process form data and save to the database
            # Assuming you have a Student model for storing student information
            student = Student(
                branch=form.cleaned_data['branch'],
                name=form.cleaned_data['name'],
                surname=form.cleaned_data['surname'],
                dateOfBirth=form.cleaned_data['dateOfBirth'],
                image=form.cleaned_data['image'],
                
            )
            
            student.save()

            # Create dataset for face recognition
            student.imageDataSet = create_dataset(student.name)  # Replace with actual username extraction logic
            student.matricule = generate_matricule(student)
            student.save()
            messages.success(request, 'Student registered successfully.')
            return redirect('preinscription')

    else:
        form = StudentRegistrationForm()

    return render(request, 'students/student_registration.html', {'form': form})


