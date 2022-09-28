from django.shortcuts import render
from .models import *


def test(request):
    return render(request, "testapp/test.html", {'rubrics': Rubric.objects.all()})

def get_rubric(request, rubric_id):
    rubric = Rubric.objects.get(pk=rubric_id)
    return render(request, "testapp/rubric.html", {'rubric': rubric})
