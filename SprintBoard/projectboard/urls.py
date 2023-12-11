from django.urls import path
from projectboard import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.projectboard, name="ProjectBoard"),
    path('create/', views.projectdetail, name='ProjectDetail'),
    path('create/<projectname>/', views.projectcreate, name='ProjectCreate'),
]

urlpatterns += staticfiles_urlpatterns()