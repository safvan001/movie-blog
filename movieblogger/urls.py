"""
URL configuration for movieblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from movieblogger import views
app_name='movieblogger'

urlpatterns = [
    # path('',views.base,name='base'),
    path('',views.MovieListView.as_view(),name='base'),
    # path('add/',views.add,name='add'),
    path('add/',views.MovieaddView.as_view(),name='add'),
    # path('veiw/<int:p>',views.veiw,name='veiw'),
    path('veiw/<int:pk>',views.MovieDetailView.as_view(),name='veiw'),

    path('update/<int:p>',views.update,name="update"),
    path('delete/<int:p>',views.delete,name="delete"),

]
