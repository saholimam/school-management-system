from django.urls import path

from .views import home_page, about_page, student_page


urlpatterns = [
    path('', home_page, name= 'home_page'),
    path('home/', home_page, name='home_page'),
    path('about/', about_page, name= 'about_page'),
    path('student/', student_page, name= 'student_page'),
]
