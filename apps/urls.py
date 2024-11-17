from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home),
    path('about/',views.About),
    path('service/',views.Service),
    path('project/',views.Project),
    path('blog/',views.Blog),
    path('contact/',views.Contact),
    path('feature/',views.Feature),
    path('team/',views.Team),
    path('testimonial/',views.Testimonial),
]
