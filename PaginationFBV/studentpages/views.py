from django.shortcuts import render
from .models import Student
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.

def showpages(request):
    record=Student.objects.all()
    paginate=Paginator(record,4)
    page_show=request.GET.get('page')

    try:
        posts=paginate.page(page_show)
    except PageNotAnInteger:
        posts=paginate.page(1)
    except EmptyPage:
        posts=paginate.page(paginate.num_pages)

    return render(request, 'show.html', {'posts': posts})