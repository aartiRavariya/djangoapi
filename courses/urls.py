from django.urls import path, include
from . import views
from rest_framework import routers # routers allows us to create GET and POST request. GET req gets the thing, shows it on screen. POST req post something in the db

router = routers.DefaultRouter()
router.register('courses', views.CourseView) # 'courses' is the url we want to show

urlpatterns = [
    path('', include(router.urls)), # '' means home page
]
