from django.urls import path, re_path
from projectboard import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.shortcuts import redirect
from django.views.generic import RedirectView


urlpatterns = [
    path("", views.home, name="Home"),
    path('account/', views.account, name='Account'),
    path('projects/', views.projects, name='Projects'),
    path('create/', views.create, name='CreateProject'),
    path('create/<projectname>', views.createproject, name='CreateProject'),
    # path('<path:unknown_path>', RedirectView.as_view(url='/', permanent=False), name='catch-all'),
    path('createissue/', views.createissue, name='createissue'),
    path('updateissue/<int:issue_id>/', views.updateissue, name='updateissue'),
    path('deleteissue/<int:issue_id>/', views.deleteissue, name='deleteissue'),
    re_path(r'^.*$', RedirectView.as_view(url='/', permanent=False), name='catch-all'),
]

urlpatterns += staticfiles_urlpatterns()