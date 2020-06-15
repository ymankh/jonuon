from django.shortcuts import render
from django.core.paginator import Paginator
from time import asctime

from .models import Material, Specialty, Doctor, Course, University


def passing_arguments(materials):
    return {
        "materials": materials,
        "doctor_choices": Doctor.objects.all(),
        "coerce_choices": Course.objects.all(),
        "specialty_choices": Specialty.objects.all(),
        "universities": University.objects.all(),
        'years': [a for a in range(2000, int(asctime()[-4:]) + 1)],
        "semesters": ("first semester", "second semester", "summer semester")
    }


def paginate(request, q_set, pr_page):
    paginator = Paginator(q_set, pr_page)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)


def all_materials(request):
    materials = Material.objects.all().order_by("-pk")
    materials = paginate(request, materials, 12)
    passed_arguments = passing_arguments(materials)
    return render(request, "all_courses.html", passed_arguments)


def material_search_result(request):
    materials = Material.objects.all()
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            materials = materials.filter(title__icontains=keywords)
    if 'Doctor' in request.GET:
        materials = materials.filter(doctor=request.GET['Doctor'])
    if "coerce" in request.GET:
        materials = materials.filter(course=request.GET["coerce"])
    if "specialty" in request.GET:
        materials = materials.filter(specialty=request.GET["specialty"])
    if "University" in request.GET:
        materials = materials.filter(university=request.GET["University"])
    if "year" in request.GET:
        materials = materials.filter(year=request.GET["year"])
    if "semester" in request.GET:
        materials = materials.filter(semester=request.GET["semester"])

    materials = materials.order_by('-id')
    materials = paginate(request, materials, 12)
    passed_arguments = passing_arguments(materials)
    return render(request, 'all_courses.html', passed_arguments)
