from django.contrib import admin
from .models import Material, Course, Doctor,\
                    Specialty, University


class AdminMatirials(admin.ModelAdmin):
    pass


admin.site.register(Material, AdminMatirials)


class AdminCourses(admin.ModelAdmin):
    pass


admin.site.register(Course, AdminCourses)


class AdminDoctors(admin.ModelAdmin):
    pass


admin.site.register(Doctor, AdminDoctors)


class AdminSpecialty(admin.ModelAdmin):
    pass


admin.site.register(Specialty, AdminSpecialty)


class AdminUniversity(admin.ModelAdmin):
    pass


admin.site.register(University, AdminUniversity)
