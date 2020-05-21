from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.HyperlinkedModelSerializer): # HyperlinkedModelSerializer is used to get the url of each item and that is passed in the url in the fields
    class Meta:
        model = Course
        fields = ('id', 'url', 'name', 'language', 'price')

        #translates our data from to and from json (takes our data from db and serializes to json which is most used to create pi and to send around the internet)