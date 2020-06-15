from django.db import models
from time import asctime
from django.utils import timezone


def current_year():
    return asctime()[-4:]


class Specialty(models.Model):
    name = models.CharField(max_length=250, default="")

    def __str__(self):
        return self.name


class University(models.Model):
    name = models.CharField(max_length=250, default="")

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Material(models.Model):
    type_options = (
        ("LectureNotes", "LectureNotes"),
        ("Exam form", "Exam form"),
        ("Worksheet", "Worksheet"),
        ("Book", "Book"),
        ("Syllabus", "Syllabus")
    )
    semesters = (
        ("first semester", "first semester"),
        ("second semester", "second semester"),
        ("summer semester", "summer semester")
    )
    title = models.CharField(max_length=255)
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True)
    specialty = models.ForeignKey(Specialty, on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    material_type = models.CharField(max_length=60, choices=type_options)
    year = models.PositiveIntegerField(default=current_year)
    semester = models.CharField(choices=semesters, max_length=20)
    link = models.URLField(max_length=500)
    image = models.ImageField(default="defult_material_img.jpg", upload_to=f"cources")
    publish_date = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.title


class MainPhoto(models.Model):
    photo = models
