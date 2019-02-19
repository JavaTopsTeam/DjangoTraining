from django.urls import path,include
from . import views

urlpatterns = [

    path('indexpage/',views.indexPage,name="indexpage"),
    path('details',views.index,name="details"),
    path('addtrainer/',views.addtrainer,name="addtrainer"),
    path('addpage/',views.addtrainerPage,name="addpage"),
    path('update/', views.update, name='update'),
    path('insert/', views.insert, name='insert'),
    path('store/', views.store, name='store'),

]
