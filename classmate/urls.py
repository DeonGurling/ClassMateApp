from django.contrib import admin
from django.urls import include, path
from main import views

from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

app_name = 'main'
app_name = 'quizzes'


urlpatterns = [
    path('', include('main.urls')),
    path('', include('quizzes.urls')),
    path('admin/', admin.site.urls),
    path('student/sign_up', views.student_sign_up,
         name='student-sign-up'),
    #path('educator/sign_up', views.educator_sign_up,
         #name='educator-sign-up'),
    #path('educator/sign-in/', auth_views.LoginView.as_view(template_name='educator/sign-in.html'),
         #name='educator-sign-in'),
    #path('educator/sign-out/', auth_views.LogoutView.as_view(next_page='/'),
         #name='educator-sign-out'),
    path('educator/', views.educator_home, name='educator-home'),
    path('educator/upload/', views.ed_upload, name='upload'),
    path('educator/assignments', views.assignment_list, name='assignment_list'),
    path('educator/upload_assignments', views.upload_assignment, name='upload_assignment'),
    path('educator/assignments/<int:pk>/', views.delete_assignment, name='delete_assignment'),
    path('student/sign-in/', auth_views.LoginView.as_view(template_name='student/sign-in.html'),
         name='student-sign-in'),
    path('student/sign-out/', auth_views.LogoutView.as_view(next_page='/'),
         name='student-sign-out'),
    path('student/', views.student_home, name='student-home'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


