from django.shortcuts import render
from Sourcemodel.models import Source


def index(request):
    source = Source.objects.all()
    return render(request, "index.html", {
        "source": source
    })


def create(request):
    return render(request, "source_c.html")


def update(request):
    return render(request, "source_u.html")


def delete(request):
    return render(request, "source_d.html")


def get_by_id(request, id):
    source = Source.objects.get(pk=id)
    return render(request, "get_by_id.html", {
        "source": source
    })