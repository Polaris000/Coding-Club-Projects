from django.contrib import admin
from .models import Section, Student

# display given models on admin site
admin.site.register(Section)
admin.site.register(Student)