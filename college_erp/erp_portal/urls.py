from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('hostel/',views.hostel,name='hostel'),
    path('admission_procedure/',views.admission_procedure,name='admission_procedure'),
    path('library/',views.library,name='library'),
    path('audi/',views.audi,name='audi'),
    path('overview/',views.overview,name='overview'),
    path('socialrespons/',views.socialrespons,name='socialrespons'),
    path('sports/',views.sports,name='sports'),
    path('campus/',views.campus,name='campus'),
    path('lab/',views.lab,name='lab'),
    path('dispensary/',views.dispensary,name='dispensary'),
    path('achievements/',views.achievements,name='achievements'),
    path('rulesandregulation/',views.rulesandregulation,name='rulesandregulation'),
    path('apply/',views.apply,name='apply'),
    path('login/',views.login1,name='login'),
    path('teacherlogin/<int:t_id>',views.teacherlogin,name='teacherlogin'),
    path('studentlogin/<int:s_id>',views.studentlogin,name='studentlogin'),
    path('hod/',views.hod,name='hod'),
    path('info/',views.detail,name='detail'),


    path('staff_take_attendance/<int:pk>', views.staff_take_attendance,name="staff_take_attendance"),
    path('get_students/<int:pk>', views.get_students, name="get_students"),
    path('save_attendance_data', views.save_attendance_data, name="save_attendance_data"),
    path('staff_update_attendance/<int:pk>', views.staff_update_attendance, name="staff_update_attendance"),
    path('get_attendance_dates/<int:pk>', views.get_attendance_dates, name="get_attendance_dates"),
    path('get_attendance_student/<int:pk>', views.get_attendance_student, name="get_attendance_student"),
    path('save_updateattendance_data', views.save_updateattendance_data, name="save_updateattendance_data"),

    path('student_view_attendance/<int:pk>', views.student_view_attendance,name="student_view_attendance"),
    path('student_view_attendance_post/<int:pk>', views.student_view_attendance_post,name="student_view_attendance_post"),

    path('staff_add_result/<int:pk>', views.staff_add_result, name="staff_add_result"),
    path('save_student_result/', views.save_student_result, name="save_student_result"),
    path('student_view_result/<int:pk>', views.student_view_result, name="student_view_result"),
   # path('chooseclass/',views.chooseclass),
    #path('timetable/',views.generate),
    path('courses_offered/',views.courses_offered,name='courses_offered'),
    path('R&D/',views.RD,name='R&D'),
    path('fees/',views.fees,name='fees'),
    path('placement/',views.placement,name='placement'),
    path('edcell/',views.edcell,name='edcell'),
    path('training/',views.training,name='training'),
    path('aoverview/',views.Aoverview,name='aoverview'),
    path('Epros/',views.Epros,name='Epros'),
    path('ac/',views.ac,name='ac'),
    path('scholarship/',views.scholarship,name='scholarship'),
    path('cs/',views.cs,name='cs'),
    path('it/',views.it,name='it'),
    path('mech/',views.mech,name='mech'),
    path('ece/',views.ece,name='ece'),
    path('ele/',views.ele,name='ele'),
    path('ash/',views.ash,name='ash'),
    path('bba/',views.bba,name='bba'),
    path('mba/',views.mba,name='mba'),
    path('bca/',views.bca,name='bca'),
    path('mca/',views.mca,name='mca'),



   

]