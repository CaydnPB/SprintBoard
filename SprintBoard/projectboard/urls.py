from django.urls import path
from projectboard import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.home, name="Home"),
    path('account/', views.account, name='Account'),
    path('projects/', views.projects, name='Projects'),
    path('create/', views.create, name='CreateProject'),
    path('create/<projectname>/', views.createproject, name='CreateProject'),
]

urlpatterns += staticfiles_urlpatterns()