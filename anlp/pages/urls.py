from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name="index"),
    path('home', views.home, name='home'),
    path('model', views.model, name='model'),
    #path('model2', views.model2, name='model2')
]
