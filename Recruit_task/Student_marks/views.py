from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Section, Student

# main webpage display view
def index(request):
   all_sections = Section.objects.all()
   student_name = Student.student_name

   required = {
     'all_sections': all_sections,
     'student_name': student_name, 
   }
   return render(request, 'Student_marks/index.html', required)


# increases marks after clicking link button 
# based on if conditions
def extra_view(request):
   all_students = Student.objects.all()

   for student in all_students:
     if 29 <= student.student_score <= 35:
         student.student_score += 7
         student.save()
   return HttpResponseRedirect("/")
