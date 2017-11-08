from django.db import models


class Section(models.Model):
   section_name = models.CharField(max_length=100)

   def __str__(self):
      return self.section_name


class Student(models.Model):
   sec = models.ForeignKey(Section, on_delete=models.CASCADE)
   student_name = models.CharField(max_length=100)
   student_score = models.IntegerField(default=0)

   def __str__(self):
      return self.student_name + "-" + str(self.student_score)


