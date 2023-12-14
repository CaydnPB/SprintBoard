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
    path('create_issue/', views.create_issue, name='create_issue'),
    path('update_issue/<int:issue_id>/', views.update_issue, name='update_issue'),
    path('delete_issue/<int:issue_id>/', views.delete_issue, name='delete_issue'),
    re_path(r'^.*$', RedirectView.as_view(url='/', permanent=False), name='catch-all'),
]

urlpatterns += staticfiles_urlpatterns()