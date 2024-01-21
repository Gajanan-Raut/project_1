from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q
from shoppingapp.models import Task
from shoppingapp.models import Course
from shoppingapp.form import emp
from shoppingapp.form import stus,stud
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.

def home(request):

    # return HttpResponse('hello world')
    return render(request,'home.html')

def index(request):
    content={}
    content['data']=Task.objects.filter( is_deleted='N')
    # print(content['data'])

    
    return render(request,'index.html',content)
   


def base(request):
    return render(request,'base.html')

def evenodd(request,n):
    num= int(n)%2
    d={'res':num}
    return render(request,'index.html',d)


def about(request):
    return render(request,'about.html')


def create_task(request):
    if request.method=='POST':
        t=request.POST['t']
        det=request.POST['det']
        dt=request.POST['dt']

        # print(t)
        # print(det)
        # print(dt)
        t1=Task.objects.create(title=t,datails=det,date=dt,is_deleted='N')
        # print(t1)
        t1.save()
        return redirect('/index')
    
    else:

        return render(request,'create_task.html')
    

def delete(request,d):
    # x = Task.objects.get(id=d)
    # x.delete()

    x=Task.objects.filter(id=d)
    x.update(is_deleted = 'Y')
    return redirect('/index')

def edit(request,n):
    if request.method=='POST':
        ut=request.POST['t']
        udet=request.POST['det']
        udt=request.POST['dt']


        # print(ut)
        # print(udet)
        # print(udt)
        x=Task.objects.filter(id=n)
        x.update(title=ut,datails=udet,date=udt)
        return redirect('/index')


    else: 
       content={}
       content['data']=Task.objects.filter(id=n)
       return render(request,'editform.html',content)
    

def dashboard(request):
    if request.method=='POST':
        c=request.POST['c']
        d=request.POST['d']
        ca=request.POST['cat']
        p=request.POST['pt']


        # print(c)
        # print(d)
        # print(ca)
        # print(p)
        x=Course.objects.create(cname=c,cdur=d,ccat=ca,cprice=p,is_deleted='N')
        x.save()
        return redirect('/cdashboard')
    else:
        return render(request,'dashboard.html')
    

def cdashboard(request):
    context={}
    # context['data']=Course.objs.filter(is_deleted='N')
    context['data']=Course.objects.filter(is_deleted='N')
    # context['data']=Course.objects.filter(is_deleted='N',ccat="Data Science")
    # context['data']=Course.objects.filter(cprice__gt=20000)
    # context['data']=Course.objects.filter(cprice__gte=20000)
    # context['data']=Course.objects.filter(cprice__lt=20000)
    # context['data']=Course.objects.filter(cprice__lte=20000)
    # print(context['data'])
    # context['data']=Course.objects.filter(ccat="Data Science",cprice__gt=20000)
    # Q1=Q(ccat="Data Science")
    # Q2=Q(cprice__gt=20000)
    # context['data']=Course.objects.filter(Q1&Q2)
    # Q1=Q(cdur=40)
    # Q2=Q(cdur=20)
    # Q3=Q(cdur=50)
    # context['data']=Course.objects.filter(Q1|Q2|Q3)
    # context['data']=Course.objects.order_by('cdur')
    # context['data']=Course.objects.order_by('-cdur')
    # context['data']=Course.objects.order_by('cprice')
    # context['data']=Course.objects.order_by('cprice').filter(is_deleted='N',ccat="Data Science")


    return render(request,'cdashboard.html',context)
def lowtohigh(request):
    context={}
    context['data']=Course.objects.filter(is_deleted='N').order_by('cprice')
    return render(request,'cdashboard.html',context)

def hightolow(request):
    context={}
    context['data']=Course.objects.filter(is_deleted='N').order_by('-cprice')
    return render(request,'cdashboard.html',context)

def deleted(request,n):
    
    # x=Course.objects.get(id=n)
    # x.delete()

    x=Course.objects.filter(id=n)
    x.update(is_deleted = 'Y')


    return redirect('/cdashboard')

def edits(request,n):

    if request.method=='POST':
        c=request.POST['c']
        cdurs=request.POST['d']
        ccats=request.POST['cat']
        cprices=request.POST['pt']
        x=Course.objects.filter(id=n)
        x.update(cname=c,cdur=cdurs,ccat=ccats,cprice=cprices)
        return redirect('/cdashboard')

    else:
        context={}
        context['data']=Course.objects.filter(id=n)
        #print(context['data'])
        return render(request,'edits.html',context)
    
def emps(request):
    context={}
    context['data'] = emp
    return render(request,'forms.html',context)
        
def studs(request):
    context={}
    context['stud']=stus
    return render(request,'studforms.html',context)

def stude(request):
    context={}
    context['forms']=stud
    return render(request,'cform.html',context)


class cview(View):
    def get(self,request):
        return HttpResponse('hello world get claa')

    def post(self,request):
        cname=request.POST['names']
        cage=request.POST['age']
        caddress=request.POST['address']
        print(cname)
        print(cage)
        print(caddress)
    
def resiter(request):
    if request.method=='POST':
        uname=request.POST['username']
        pas=request.POST['password1']
        # print(uname)
        # print(password)
        f1=User(username=uname,password=pas,is_staff=True,is_active=True)
        f1.save()
        return redirect('/register')
    else:
        fm=UserCreationForm()
        return render(request,'signup.html',{'form':fm})
    
def navbar(request):
    return render(request,'navbar.html')