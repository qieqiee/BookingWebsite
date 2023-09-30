from django.shortcuts import render;
from django.http import HttpResponse,HttpResponseRedirect;
from project.models import Student,Felo, Washingmachine, Book
from django.db.models import Q;
from django.urls import reverse;

# Create your views here.
def index(request):
    return render(request, 'index.html')

def registerpage(request):
    if request.method == 'POST':
        studentid = request.POST.get('studentid')
        studentname = request.POST.get('studentname')
        studentphone = request.POST.get('studentphone')
        
        data = Student(studentid=studentid, studentname = studentname, studentphone= studentphone) 

        data.save()
       
        return HttpResponseRedirect('login')
    else:
        return render(request,'registerpage.html')

def login(request):
    if request.method == 'POST':
        studentid = request.POST.get('studentid')
        studentphone = request.POST.get('studentphone')
        data = Student.objects.filter(studentid=studentid)
        student = data.first()
        phone = student.studentphone

        datalen = Student.objects.filter(studentid=studentid)
        

        if len(datalen)!= 0:
            if studentphone==phone and len(datalen) != 0:
                
                return HttpResponseRedirect('mainpage')

            elif studentphone != phone and len(datalen) != 0:
                dict={
                    'message' : 'incorrect no phone'
                }
                return render(request,'login.html',dict)
        else:
            dict={
                    'message' : 'register first!!!!'
            }
            return render(request,'login.html',dict)
       
        
    else:
        return render(request,'login.html')

def felo(request):
    if request.method == 'POST':
        feloid = request.POST.get('feloid')
        password = request.POST.get('password')
        data = Felo.objects.filter(feloid=feloid).first()
        if data is not None:
            if password == data.password:
                return HttpResponseRedirect('displaystud')
            elif password != data.password:
                dict={
                'message' : "access denied"
            }
            return render(request,'felo.html',dict)
             
                
        elif data is None:
            dict={
                'message' : "access denied"
            }
            return render(request,'felo.html',dict)
            
    else:
        return render(request,'felo.html')

def mainpage(request):
    if request.method == 'POST': 
        #studentid = request.POST.get('studentid')
        machineNo = request.POST.get('machineNo')
        machineLocation = request.POST.get('machineLocation')
        laundrydate = request.POST.get('laundrydate')
        starttime = request.POST.get('starttime')
        endtime = request.POST.get('endtime')
        machine=Washingmachine.objects.get(machineNo=machineNo)
        studentid = request.POST.get('studentid')
        student = Student.objects.get(studentid=studentid)
       

        #data=Booking.objects.filter(machineNo=machineNo,laundrydate=laundrydate,starttime=starttime,endtime=endtime)
        #data2 = Washingmachine.objects.filter(machineLocation=machineLocation)
        data = Book.objects.filter(machineNo=machine,laundrydate=laundrydate,starttime=starttime,endtime=endtime)

        datalen = len(data)
        if datalen == 0:
            data2 = Book(machineNo=machine, studentid=student, laundrydate=laundrydate,starttime=starttime,endtime=endtime)
            data2.save()
            idbook=data2.id
            bookdetail=Book.objects.get(id=idbook)
            dict={
                'message' : 'Booked',
               #'studentid' : studentid,
                'machineNo' : machineNo,
                'machineLocation' : machineLocation,
                'laundrydate' : laundrydate,
                'starttime ' : starttime,
                'endtime' : endtime,
                'machine':machine,
                'id':idbook,
                'bookdetail':bookdetail
                #'data2' : data2
            }
            
            return render(request, 'mainpage.html',dict)
        else:
            dict={
                'message' : 'NOT Available',
            }

        return render(request, 'mainpage.html',dict)

    else:
        return render(request, 'mainpage.html')

def success(request,code):
    bookdetail=Book.objects.get(id=code)
    dict={
        'bookdetail':bookdetail
    }
    return render(request, 'success.html',dict)

def displaystud(request):
    alldata=Student.objects.all()
    dict={
        'alldata': alldata
    }
    return render(request,'displaystud.html',dict)
 
def updatestudent(request,studentid):
    data = Student.objects.get(studentid=studentid)
    dict={
        'data' : data
    }
    return render (request, "updatestudent.html",dict)

def save_updatestudent(request,studentid):
    studentname=request.POST.get('studentname')
    studentphone=request.POST.get('studentphone')
    data=Student.objects.get(studentid=studentid)
    #data.studentname=studentname
    data.studentphone=studentphone
    data.save()
    return HttpResponseRedirect(reverse('displaystud'))


def deletestudent(request,studentid):
    data = Student.objects.get(studentid=studentid)
    data.delete()
    return HttpResponseRedirect(reverse("displaystud"))
 
def displaybooking(request):
    alldata=Book.objects.all()
    dict={
        'alldata': alldata
    }
    return render(request,'displaybooking.html',dict)
 
def updatebooking(request,id):
    data = Book.objects.get(id=id)
    dict={
        'data' : data
    }
    return render (request, "updatebooking.html",dict)

def save_updatebooking(request,id):
    studentid=request.POST.get('studentid')
    machineNo=request.POST.get('machineNo')
    starttime = request.POST.get('starttime')
    endtime = request.POST.get('endtime')
    laundrydate=request.POST.get('laundrydate')
    data=Book.objects.get(id=id)
    #data.studentid=studentid
    #data.starttime=starttime
    #data.endtime=endtime
    data.laundrydate=laundrydate
    data.save()
    return HttpResponseRedirect(reverse('displaybooking'))


def deletebooking(request,id):
    data = Book.objects.get(id=id)
    data.delete()
    return HttpResponseRedirect(reverse("displaybooking"))

