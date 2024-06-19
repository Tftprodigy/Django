from django.urls import path
##Importing path in urls
# path helps us import multiple urls
from . import views #views import

urlpatterns = [
    path('', views.index, name='index')
    
]
# urlpatterns is a list created to contain all the urls in the
# in the project.
#when the first '' is empty in the path, its spefifys the 
#root url.

# import views



