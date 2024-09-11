from django.urls import path
from home.views import *
# urls.py
urlpatterns = [
    # PAGES
    path("",index,name='index'),
]