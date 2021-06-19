from django.contrib import admin
from .models import *

admin.site.register(application)

admin.site.register(UserProfile)

admin.site.register(Dept)

admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Assign)
admin.site.register(SubjectAssign)
admin.site.register(Class)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(SessionYearModel)
admin.site.register(StudentResult)




# Register your models here.
