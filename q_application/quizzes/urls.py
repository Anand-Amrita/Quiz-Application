from django.urls import path
from . import views

urlpatterns = [
    # User Authentication
    path('', views.front_page, name='front_page'),  # Front page
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Admin Views
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('manage_users/', views.manage_users, name='manage_users'),
    path('add_subjects/', views.add_subjects, name='add_subjects'),
    path('view_results/', views.view_results, name='view_results'),
    path('manage_subjects/', views.manage_subjects, name='manage_subjects'),
    path('search_student/', views.search_student, name='search_student'),
    
    # Student Views
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('student_settings/', views.student_settings, name='student_settings'),
    path('user_results/', views.user_results, name='user_results'),
    
    # Quiz Views
    path('quiz_page/<int:subject_id>/', views.quiz_page, name='quiz_page'),
    path('quiz_selection/', views.quiz_selection, name='quiz_selection'),

    # Search Student (Admin)
    
]
