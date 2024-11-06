from django.urls import path

from main import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin_dash', views.admin_home, name='admin_home'),
    path('educator/sign-in', auth_views.LoginView.as_view(),{'template_name': 'educator/sign-in.html'},
         name='educator-sign-in'),
    path('educator/sign-out', auth_views.LogoutView.as_view,
         {'next_page': '/'},
         name='educator-sign-out'),

    path('student/sign-in', auth_views.LoginView.as_view(),{'template_name': 'student/sign-in.html'},
         name='student-sign-in'),
    path('student/sign-out', auth_views.LogoutView.as_view,
         {'next_page': '/'},
         name='student-sign-out'),
    path('student/sign_up', views.student_sign_up,
         name='student-sign-up'),

]

