from django.urls import path
from myapp import views
app_name = 'myapp'

urlpatterns = [
    path('home/', views.home,  name = 'home'),
    path('overview/', views.overview,  name = 'overview'),
    path('history/', views.history,  name = 'history'),
    path('project/', views.project,  name = 'project'),
    path('research/', views.research,  name = 'research'),
    path('contact/', views.contact,  name = 'contact')
]
