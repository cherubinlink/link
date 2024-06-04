from django.urls import path
from service import views


urlpatterns = [
    path('', views.index,name='index'),
    
    # marketing
    path('marketing',views.marketing,name='marketing'),
    
    # web
    path('web',views.web, name='web'),
    
    # cloud
    path('cloud',views.cloud, name='cloud'),
    
      # donnes
    path('donne',views.donne, name='donne'),
]
