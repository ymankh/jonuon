from django.contrib import admin
from .models import Material, Course, Doctor


class AdminMatirials(admin.ModelAdmin):
    pass


admin.site.register(Material, AdminMatirials)


class AdminCourses(admin.ModelAdmin):
    pass


admin.site.register(Course, AdminCourses)


class AdminDoctors(admin.ModelAdmin):
    pass


admin.site.register(Doctor, AdminDoctors)
