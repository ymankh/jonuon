from django.db import models
from time import asctime


def current_year():
    return asctime()[-4:]


class Specialty(models.Model):
    name = models.CharField(max_length=250, default="")


class Course(models.Model):
    name = models.CharField(max_length=100)


class Doctor(models.Model):
    name = models.CharField(max_length=100)


class Material(models.Model):
    type_options = (
        ("LuctuerNotes", "LuctuerNotes"),
        ("Exam form", "Exam form"),
        ("Worcksheet", "Worcksheet"),
        ("Book", "Book"),
        ("Syllabus", "Syllabus")
    )
    semesters = (
        ("first semester", "first semester"),
        ("second semester", "second semester"),
        ("summer semester",  "summer semester")
    )
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    material_type = models.CharField(max_length=60, choices=type_options)
    year = models.PositiveIntegerField(default=current_year)
    semester = models.CharField(choices=semesters, max_length=20)
    link = models.URLField(max_length=500)

    def __str__(self):
        return self.title
