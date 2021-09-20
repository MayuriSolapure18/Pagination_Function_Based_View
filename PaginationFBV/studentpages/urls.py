from django.urls import path
from .views import showpages

urlpatterns=[
    path('v1/',showpages)
]