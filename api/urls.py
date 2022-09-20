from django.contrib import admin
from django.urls import path
from DRFAPI import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stuInfo/<int:pk>', views.student_detail),
    path('stuInfo/', views.student_list),
    
    path('addStuInfo/', views.student_create),
    path('studentAPI/', views.student_api),
]
