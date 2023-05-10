from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import City,StateName,VaccineCentre,AppointmentDetails
from django.contrib import messages
import datetime

@login_required(login_url='login')
def home(request):
    datetoday=datetime.date.today
    statelist=StateName.objects.all().order_by('name')
    cities=[]
    centres=[]
    start_hour=''
    end_hour=''
    if request.method=='POST':
        name=request.POST['name']
        mobile=request.POST['mobile']
        centre=request.POST['centre']
        centreObj=VaccineCentre.objects.filter(name=centre)[0]
        email=request.user.email
        date=request.POST['bookingdate']
        total_booking=len(AppointmentDetails.objects.filter(date=date).filter(centre=centreObj))
        index=total_booking+1
        if (total_booking<10):
            ins=AppointmentDetails(name=name,mobile=mobile,centre=centreObj,email=email,date=date,index=index)
            ins.save()
            messages.info(request,"Appointment booked successfully for "+date+"!")


    if request.is_ajax():
        cities=City.objects.filter(state=request.GET.get('statename')).order_by('name')
        if request.GET.get('city')!=None:
            centres=VaccineCentre.objects.filter(city=request.GET.get('city'))
            context={'cities':cities,'states':statelist,'centres':centres,'start_hour':start_hour,'end_hour':end_hour,'datetoday':datetoday}
            return render(request,'centreDD.html',context)
        context={'cities':cities,'states':statelist,'centres':centres,'start_hour':start_hour,'end_hour':end_hour,'datetoday':datetoday}
        return render(request,'citywithValue.html',context)
    context={'cities':cities,'states':statelist,'centres':centres,'start_hour':start_hour,'end_hour':end_hour,'datetoday':datetoday}
    return render(request,'home.html',context)


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        context = {'form':form}
        if request.method == 'POST':        
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        return render(request,'signup.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
        return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')