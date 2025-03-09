from django.urls import path
from database import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup_user, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('reviwes/', views.reviwes_user, name='reviwes'),
    path('tables/', views.tables, name='tables'),
    path('analitics/', views.analitycs_user, name='analytics'),
    path('logout/', views.logout_user, name='logout'),
    path('edit/', views.edit_profile_user, name='edit'),
    path('add_marks/', views.add_marks_user, name='add_marks'),
    path('sprofile/', views.student_profile_user, name='student_profile'),
    path('list/', views.save_marks, name='list'),
    path('host/', views.spcam_admin, name='SPCAM Admin'),
    path('submit_admission_form/', views.admission_form_view, name='submit_admission_form'),
    path('get_subjects/', views.get_subjects, name='get_subjects'),
    path('get_students/', views.get_students, name='get_students'),
     path('add_teacher/', views.add_teacher, name='add_teacher'),
    # path('faculty_details/', views.faculty_details, name='faculty_details'),
    path('student_marks/', views.create_class_subjects, name='student_marks'),
    path('add_subjects/', views.class_subject_add, name='add_subjects'),
    path('v_student_profile/', views.view_student_profile, name='v_student_profile'),
]

