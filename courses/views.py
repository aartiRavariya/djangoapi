from django.shortcuts import render
from rest_framework import viewsets         # viewsets are set of pages that is gonna to create for us
from .models import Course
from .serializers import CourseSerializer

# views in django are alwys the webpages views are the brains behind the scenes
# that tells django what to do with the webpages
# normally u have to create function for each webpages you wan to built

class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()          # queryset is the model our db and need to pull out the data out of the db, just call the name of the model
    serializer_class = CourseSerializer     # what serialzer class should be used (converts the data from db to and from json)