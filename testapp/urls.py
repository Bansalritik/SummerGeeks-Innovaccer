from django.urls import path, include
from testapp import views

# url imported to access the view to be rendered and to access the page
urlpatterns = [
    path('', views.Course, name="home_page"),
]