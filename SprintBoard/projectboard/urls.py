from django.urls import path, re_path
from projectboard import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.shortcuts import redirect
from django.views.generic import RedirectView


urlpatterns = [
    path("", views.home, name="Home"),
    path('account/', views.account, name='Account'),
    # path('projects/', views.projects, name='Projects'),
    path('createproject/', views.createproject, name='createproject'),
    path('updateproject/<int:project_id>/', views.updateproject, name='updateproject'),
    path('deleteproject/<int:project_id>/', views.deleteproject, name='deleteproject'),
    path('createissue/', views.createissue, name='createissue'),
    path('updateissue/<int:issue_id>/', views.updateissue, name='updateissue'),
    path('deleteissue/<int:issue_id>/', views.deleteissue, name='deleteissue'),
    path('updateissuestatus/<int:issue_id>/<str:new_status>/', views.updateissuestatus, name='updateissuestatus'),
    path('projects/', views.projects, name='projects'),
    path('projects/<int:project_id>/', views.projectsdetail, name='projectsdetail'),
    re_path(r'^.*$', RedirectView.as_view(url='/', permanent=False), name='catchall'),
]

urlpatterns += staticfiles_urlpatterns()