from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('',  views.login_view, name='login'),
    path('<int:id>/', views.student_form, name='student_update'),
    path('delete/<int:id>/', views.student_delete, name='student_delete'),
    path('add/', views.student_form, name='student_insert'),
    path('list/', views.student_list, name='student_list'),
]
