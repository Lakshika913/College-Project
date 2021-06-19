from typing import List
from django.contrib import messages, auth
from django.http.request import validate_host
from django.shortcuts import render, redirect, reverse
from .models import *
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect, response
from django.views.decorators.csrf import csrf_exempt
import json
import datetime
from django.conf import settings 
from django.core.mail import EmailMessage
from django.template.loader import render_to_string



def index(request):
    return render(request,"frontpage.html")
def hostel(request):
    return render(request,"hostel.html")
def admission_procedure(request):
    return render(request,"admission_procedure.html")
def library(request):
    return render(request,"library.html")
def audi(request):
    return render(request,"audi.html")
def overview(request):
    return render(request,"overview.html")
def socialrespons(request):
    return render(request,"socialrespons.html")
def sports(request):
    return render(request,"sports.html")
def campus(request):
    return render(request,"campus.html")
def lab(request):
    return render(request,"lab.html")
def dispensary(request):
    return render(request,"dispensary.html")
def achievements(request):
    return render(request,"achievements.html")
def rulesandregulation(request):
    return render(request,"rulesandregulation.html")
def courses_offered(request):
    
    return render(request, 'courses_offered.html')
   
def RD(request):
    
    return render(request, 'R&D.html')

def fees(request):
    
    return render(request, 'fees.html')

def placement(request):
    return render(request, 'placement.html')

def edcell(request):
    return render(request, 'EDcell.html')

def training(request):
    return render(request, 'training.html')
def Aoverview(request):
    return render(request, 'Academicoverview.html')
   
def Epros(request):
    return render(request, 'Epros.html')

def ac(request):
    return render(request, 'academiccalender.html')
def scholarship(request):
    return render(request, 'scholarship.html')

def cs(request):
    return render(request, 'cs.html')
def it(request):
    return render(request, 'it.html')

def mech(request):
    return render(request, 'mech.html')
def ece(request):
    return render(request, 'ece.html')
def ele(request):
    return render(request, 'ele.html')
def ash(request):
    return render(request, 'ash.html')
def bba(request):
    return render(request, 'bba.html')

def mba(request):
    return render(request, 'mba.html')
def bca(request):
    return render(request, 'bca.html')
def mca(request):
    return render(request, 'mca.html')

def apply(request):
    if request.method=="POST":
        fn = request.POST['First_Name']
        ln = request.POST['Last_Name']
        dob=request.POST['Birthday_day']
        eid=request.POST['Email_Id']
        phone=request.POST['Mobile_Number']
        g1 = request.POST['Gender']
        a1 = request.POST['Address']
        c1 = request.POST['City']
        p1 = request.POST['Pin_Code']
        state=request.POST['State']
        cn=request.POST['Country']
        tenth=request.POST['ClassX_Percentage']
        twelth=request.POST['ClassXII_Percentage']
        course=request.POST['course']
        if application.objects.filter(email=eid).exists():
            messages.info(request, 'This user already exists.')
            return redirect("register/")

        elif application.objects.filter(contact=phone).exists():
            messages.info(request, 'This user already exists.')
            return redirect("register/")

        else:
            x=application.objects.create(firstname=fn,lastname=ln,tenth=tenth,twelth=twelth,email=eid,dob=dob,contact=phone,address=a1,city=c1,pincode=p1,state=state,country=cn,course=course,gender=g1)
            x.save()
            template = render_to_string('email_template.html',{'first_name':fn,'last_name':ln,'course':course})  
            email = EmailMessage(
              'Thanks For Applying in JMIT',
               template,
               settings.EMAIL_HOST_USER,
               [eid],
            )
            email.send()
            print(settings.EMAIL_HOST_USER)
            print(email)
            messages.info(request, 'Form submitted successfully.')
            return redirect("http://127.0.0.1:8000")
    return render(request,"apply.html")
@login_required
def teacherlogin(request):
    return render(request,"teacherlogin.html")
@login_required
def studentlogin(request):
    return render(request,"studentlogin.html")

def login1(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['pass']
        user = auth.authenticate(username=username,password=password)

        if user is not None and user.is_active:
            if user.userprofile.role == 'teacher':
                t_id = user.id
                print(t_id)
                t_name = user.username
                print(t_name)
                return  render(request,'teacherlogin.html',{'t_id':t_id,'t_name':t_name})
            elif user.userprofile.role == 'student':
                s_id = user.id
                print(s_id)
                s_name = user.username
                print(s_name)
                return  render(request,'studentlogin.html',{'s_id':s_id,'s_name':s_name})
            elif user.userprofile.role == 'hod':
                
                return  render(request,'hod.html')

        else:
            messages.info(request,"invalid login")
            return redirect('login')

    else:
        return render(request, "login.html")

@login_required
def hod(request):
    
    return render(request, 'hod.html')

def detail(request):
    if request.method=='POST':
        idd=Student.objects.all
        student_id = request.POST['namedrop']
        student_instance = Student.objects.get(pk=student_id)
        std = Student.objects.filter(pk=student_id).values()
        std = list(std)
        print(std)
        clsid = std[0]['class_id_id']
        print(clsid)
        subid = SubjectAssign.objects.filter(class_id=clsid).all()
        return render(request, 'info.html', {'student': subid})

'''Attendance'''
def staff_take_attendance(request,pk=None,*args,**kwargs):
    print(request.GET,request.POST)
    print(''+str(pk))
    sub = Teacher.objects.filter(user_id=pk).values()
    sub = list(sub)
    print(sub)
    tid = sub[0]['id']
    print(tid)
    Subject = Assign.objects.filter(teacher_id=tid).all()
    print(Subject)
    # session_years = SessionYearModel.objects.all()   "session_years":session_years
    return render(request,"staff_take_attendance.html",{'t_id':pk,'pk': pk,"subjects":Subject})

@csrf_exempt
def get_students(request,pk=None,*args,**kwargs):

    print('This is the teacher id '+str(pk))
    response_sub,response_class = request.POST['subject'].split(',')
    print(response_class,response_sub)
    # class_1 = Class.objects.values()
    # print(class_1)
    # class_2 = Class.objects.filter(id=response_class).values()
    # print('***'+str(class_2))
    assign_1 = Assign.objects.values()
    print(assign_1)

    
    sub = Teacher.objects.filter(user_id=pk,).values()
    sub = list(sub)
    print(sub)
    # session_year=request.POST.get("session_year")
    tea_id = sub[0]['id']
    print(tea_id)
    subject = Assign.objects.filter(teacher_id=tea_id,class_id = response_class).values()
    subject = list(subject)
    print(subject)
    subject1 = len(subject)
    print(subject1)
    clsid = subject[0]['class_id_id']
    # print(clsid)
    student_list = request.POST['subject']
    # print('-------'+str(request.POST))
    # print('******'+str(student_list))
    # student_instance = Student.objects.get(pk=student_list)
    # print(student_instance)
    students=Student.objects.filter(class_id=clsid).values()
    students = list(students)
    # print('////////////////////'+str(students))
    list_data=[]
    for i in range(len(students)):
        stdname = students[i]['name']
        # print(stdname)
        stdusn = students[i]['USN']
        # print(stdusn)
        data_small = {'USN':stdusn,'name':stdname}
        # print(data_small)
        list_data.append(data_small)


    return JsonResponse(json.dumps(list_data),content_type="application/json",safe=False)

@csrf_exempt
def save_attendance_data(request):
    response_sub,response_class = request.POST['subject_id'].split(',')
    print(response_class,response_sub)
    student_ids=request.POST.get("student_ids")
    subject_id=request.POST.get("subject_id")
    attendance_date=request.POST.get("attendance_date")
    # session_year_id=request.POST.get("session_year_id")

    print('++++++++++'+str(student_ids))
    
    
    subject_model=Subject.objects.get(name=response_sub)
    print('============='+str(subject_model))

    # session_model=SessionYearModel.object.get(id=session_year_id)
    json_sstudent=json.loads(student_ids)
    subject = Assign.objects.filter(class_id = response_class).values()
    subject = list(subject)
    print('#########################'+str(subject))
    subject1 = len(subject)
    print(subject1)
    clsid = subject[0]['class_id_id']
    print(clsid)
    
    students=Student.objects.filter(class_id=clsid).values()
    students = list(students)
    print('-------------------------'+str(students))
    try:
        attendance=Attendance(subject_id=subject_model,attendance_date=attendance_date)
        attendance.save()
        print(';;;;;;;;;;;;;;;;;;;;;;;'+str(attendance))
        att_id = Attendance.objects.get(id=attendance.id)
        print(';;;;;;;;;;;;;;;;;;;;;;;'+str(att_id))

        print(type(att_id))
        att = AttendanceReport.objects.values()
        print(att)

        for stud in range(len(json_sstudent)):
            std_usn = students[stud]['USN']
            print(type(std_usn))
            print('[[[[[[[[]]]]]]]]'+str(std_usn))
            std_status = json_sstudent[stud]['status']
            print('[[[[[[[[]]]]]]]]'+str(std_status))
            att_id1 = Attendance.objects.filter(id=attendance.id).values()
            print('++++++++++++'+str(att_id1))
            std_id = att_id1[0]['id']
            std_usn1 = Student.objects.get(USN=std_usn)
            print('...................'+str(std_usn1))
            a_id = Attendance.objects.get(id=attendance.id)
            print(a_id)
            
            attendance_report=AttendanceReport.objects.create(student_id=std_usn1,attendance_id=attendance,status=std_status)
            print('$$$$$$$$$$$$$$$'+str(attendance_report))
            attendance_report.save()
        return HttpResponse("OK")
    except Exception as e :
        print(e)
        
        return HttpResponse("ERR")

# update attendance
def staff_update_attendance(request,pk=None,*args,**kwargs):
    print(request.GET,request.POST)
    print(''+str(pk))
    sub = Teacher.objects.filter(user_id=pk).values()
    sub = list(sub)
    print(sub)
    tid = sub[0]['id']
    print(tid)
    Subject = Assign.objects.filter(teacher_id=tid).all()
    print(Subject)
    # session_years = SessionYearModel.objects.all()   "session_years":session_years
    return render(request,"staff_update_attendance.html",{'t_id':pk,'pk': pk,"subjects":Subject})

@csrf_exempt
def get_attendance_dates(request,pk=None,*args,**kwargs):
    print('This is the teacher id '+str(pk))
    response_sub,response_class = request.POST['subject'].split(',')
    print(response_class,response_sub)
    subject=request.POST.get("subject")
    print('%%%%%%%%%%%%%%%'+str(subject))
    sub = Teacher.objects.filter(user_id=pk).values()
    sub = list(sub)
    print(sub)
    tea_id = sub[0]['id']
    print(tea_id)
    # session_year_id=request.POST.get("session_year_id")
    # subject_obj=Assign.objects.get(teacher=tea_id,class_id=response_class,subj=response_sub)
    # print('--------------'+str(subject_obj))
    # session_year_obj=SessionYearModel.object.get(id=session_year_id)     "name":std_usn1,
    subject_obj=Subject.objects.get(name=response_sub)
    print('--------------'+str(subject_obj))
    class_obj = Class.objects.get(id=response_class)
    print('--------------'+str(class_obj))
    attendance=Attendance.objects.filter(subject_id=subject_obj)
    print('%%%%%%%%%%%%%%%'+str(attendance))
    attendance_obj=[]
    for attendance_single in attendance:
        data={"id":attendance_single.id,"attendance_date":str(attendance_single.attendance_date)}
        attendance_obj.append(data)

    return JsonResponse(json.dumps(attendance_obj),safe=False)

@csrf_exempt
def get_attendance_student(request,pk=None,*args,**kwargs):
    print('This is the teacher id '+str(pk))
    attendance_date=request.POST.get("attendance_date")
    print('--------------'+str(attendance_date))
    attendance=Attendance.objects.get(id=attendance_date)
    print('--------------'+str(attendance))

    attendance_data=AttendanceReport.objects.filter(attendance_id=attendance).values()
    print('--------------'+str(attendance_data))
    list_data=[]

    for student in range(len(attendance_data)):
        std_usn = attendance_data[student]['student_id_id']
        print(type(std_usn))
        print('[[[[[[[[]]]]]]]]'+str(std_usn))
        idd = attendance_data[student]['id']
        print(type(idd))
        print('[[[[[[[[]]]]]]]]'+str(idd))
        std_status = attendance_data[student]['status']
        print('[[[[[[[[]]]]]]]]'+str(std_status))
        std_usn1 = Student.objects.get(USN=std_usn)
        print('...................'+str(std_usn1))
        data_small={"id":idd,'usn':std_usn,'name':std_usn1.name,"status":std_status}
        list_data.append(data_small)
        print('@@@@@@@@@@@@@'+str(data_small))
    return JsonResponse(json.dumps(list_data),content_type="application/json",safe=False)

@csrf_exempt
def save_updateattendance_data(request):
    student_ids=request.POST.get("student_ids")
    print('++++++++++++'+str(student_ids))
    attendance_date=request.POST.get("attendance_date")
    print('++------++'+str(attendance_date))
    attendance=Attendance.objects.filter(id=attendance_date).values()
    # attendance_date1 = attendance_date[0][attendance_date]
    attendance = list(attendance)
    print('**************'+str(attendance))
    attendance_date1 = attendance[0]['attendance_date']
    print('......................'+str(attendance_date1))
    attendance_id=Attendance.objects.get(attendance_date=attendance_date1)
    print('++++++++++++'+str(attendance_id))

    json_sstudent=json.loads(student_ids)
    print('!!!!!!!!!!!!!!!!!!!!!!!!!'+str(json_sstudent))
    
    att = AttendanceReport.objects.values()
    print('++++++++++++'+str(att))
    
    try:
        for stud in json_sstudent:
             print('|||||||||||||||||||'+str(stud['id']))
             att_id,std_name,std_rollno = stud['id'].split(',')
            #  print(stud)
             print(type(att_id))
             print('++++++++++++'+str(att_id))
             print('++++++++++++'+str(std_name))
             print('++++++++++++'+str(std_rollno))
            #  std_usn1 = std_usn[0]['USN']
            #  print('````````````````````````````````'+str(std_usn1))
             student=Student.objects.get(name=std_name)
            #  print('++++++++++++'+str(std_usn))
            #  student=Attendance.objects.get(id=std_usn)
            #  student=Student.objects.values()
             print('++++---------========'+str(student))
             attendance_report=AttendanceReport.objects.get(student_id=student,attendance_id=attendance_id)
             print('~~~~~~~~~~~~~~'+str(attendance_report))
             attendance_report.status=stud['status']
             attendance_report.save()
        return HttpResponse("OK")
    except Exception as e:
        print(e)
        return HttpResponse("ERR")

def student_view_attendance(request,pk=None,*args,**kwargs):
    print('This is the student id '+str(pk))
    student=Student.objects.filter(user_id=pk).values()
    print('-------------- '+str(student))
    student_class = student[0]['class_id_id']
    print('+++++++++++'+str(student_class))
    student_sub = SubjectAssign.objects.filter(class_id=student_class).all()
    print('================'+str(student_sub))
    # course=student.course_id
    # subjects=SubjectAssign.objects.filter(course_id=course)
    return render(request,"student_view_attendance.html",{'s_id':pk,'pk': pk,"subjects":student_sub})

def student_view_attendance_post(request,pk=None,*args,**kwargs):
    
    subject_id=request.POST.get("subject")
    print('================'+str(subject_id))
    response_sub,response_class = request.POST['subject'].split(',')
    print(response_class,response_sub)
    subject_obj=Subject.objects.get(name=response_sub)
    print('================'+str(subject_obj))
    student_class=Student.objects.filter(class_id=response_class).values()
    print('------------'+str(student_class))
    stud_pk=Student.objects.filter(user_id=pk).values()
    print('------------'+str(stud_pk))
    stud_name = stud_pk[0]['name']
    print('||||||||||||||------'+str(stud_name))


    start_date=request.POST.get("start_date")
    end_date=request.POST.get("end_date")

    start_data_parse=datetime.datetime.strptime(start_date,"%Y-%m-%d").date()
    end_data_parse=datetime.datetime.strptime(end_date,"%Y-%m-%d").date()
    # subject_obj=Subject.objects.get(id=subject_id)
    # user_object1=UserProfile.objects.get(user_id=pk)
    # print('================'+str(user_object1))
    
    stud_obj=Student.objects.get(name=stud_name)
    print('================'+str(stud_obj))
    attendance=Attendance.objects.filter(attendance_date__range=(start_data_parse,end_data_parse),subject_id=subject_obj)
    print('@@@@@@@@@@@@@'+str(attendance))
    
    attendance_reports=AttendanceReport.objects.filter(attendance_id__in=attendance,student_id=stud_obj)
    print('###################'+str(attendance_reports))
    
    return render(request,"student_attendance_data.html",{'s_id':pk,'pk': pk,"attendance_reports":attendance_reports})


def staff_add_result(request,pk=None,*args,**kwargs):
    print(request.GET,request.POST)
    print(''+str(pk))
    sub = Teacher.objects.filter(user_id=pk).values()
    sub = list(sub)
    print(sub)
    tid = sub[0]['id']
    print(tid)
    Subject = Assign.objects.filter(teacher_id=tid).all()
    print(Subject)
    
    return render(request,"staff_add_result.html",{'t_id':pk,'pk': pk,"subjects":Subject})

def save_student_result(request):
    if request.method!='POST':
        return HttpResponseRedirect('staff_add_result')
    student_admin_id=request.POST.get('student_list')
    print('&&&&&&'+str(student_admin_id))
   
    assignment_marks=request.POST.get('assignment_marks')
    
    
    
    exam_marks=request.POST.get('exam_marks')
    print('*****'+str(exam_marks))
    subject_id=request.POST.get('subject')
    print('*****'+str(subject_id))
    


    student_obj=Student.objects.filter(USN=student_admin_id).values()
    print('++++++++++++'+str(student_obj))
    student_obj1 = student_obj[0]['USN']
    print('@@@@@@@@@@@@@'+str(student_obj1))
    
    response_sub,response_class = request.POST['subject'].split(',')
    print(response_class,response_sub)
    subject_obj=Subject.objects.filter(name=response_sub).values()
    print('$$$$$$'+str(subject_obj))
    subject_obj1 = subject_obj[0]['id']
    print('-------------'+str(subject_obj1))
    

    try:
        check_exist=StudentResult.objects.filter(subject_id=subject_obj1,student_id=student_obj1).exists()
        if check_exist:
            result=StudentResult.objects.get(subject_id=subject_obj1,student_id=student_obj1)
    # result = StudentResult.objects.values()
            print('#######'+str(result))
            result.subject_assignment_marks=assignment_marks
            print('!!!!!!!!!'+str( result.subject_assignment_marks))
            
            result.subject_exam_marks=exam_marks
            print('++++++++++'+str( result.subject_exam_marks))
            result.save()
            return HttpResponse("OK")
           
            messages.success(request, "Successfully Updated Result")
            return HttpResponseRedirect(reverse("staff_add_result"))
        else:
            stud_id = Student.objects.get(USN=student_obj1)
            subj_id = Subject.objects.get(id=subject_obj1)
            result=StudentResult(student_id=stud_id,subject_id=subj_id,subject_exam_marks=exam_marks,subject_assignment_marks=assignment_marks)
            print('????????'+str(result))
            result.save()
           
            messages.success(request, "Successfully Added Result")
            return HttpResponse("OK")
    except Exception as e:
        print(e)
        messages.error(request, "Failed to Add Result")
        return HttpResponse("error")

def student_view_result(request,pk=None,*args,**kwargs):
    # subject_id=request.POST.get("subject")
    # print('================'+str(subject_id))
    # response_sub,response_class = request.POST['subject'].split(',')
    # print(response_class,response_sub)
    # subject_obj=Subject.objects.get(name=response_sub)
    # print('================'+str(subject_obj))
    student=Student.objects.filter(user_id=pk).values()
    print('======='+str(student))
    usn = student[0]['USN']
    print('+++++++++++'+str(usn))
    # class_id = student[0]['class_id_id']
    # print('$$$$$$$$$$$$$'+str(class_id))
    # subj = SubjectAssign.objects.filter(class_id=class_id).values()
    # print('@@@@@@@@@@@@'+str(subj))
    # subj_name = subj[0]['subj_id']
    # print("######"+str(subj_name))
    # subjid = Subject.objects.filter(id=subj_name).values()
    # print("------------------"+str(subjid))
    # subj_idd = subjid[0]['name']
    # print('**'+str(subj_idd))
    # assign_marks=StudentResult.objects.filter(subject_id_id=subj_name).values()
    # print('$$$$$$$'+str(assign_marks))
    # stud_assign = assign_marks[0]['subject_assignment_marks']
    # print('((((('+str(stud_assign))
    # stud_exam = assign_marks[0]['subject_exam_marks']
    # print('((((('+str(stud_exam))
    studentresult=StudentResult.objects.filter(student_id=usn).all()
    print('@@@@@@@@@@@@@@@@@@@@'+str(studentresult))
    return render(request,"student_result.html",{'s_id':pk,'pk': pk,'studentresult':studentresult})

