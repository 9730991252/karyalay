from django.shortcuts import render , redirect 
from django.contrib import messages 
from sunil.models import *
from owner.models import *
from camera.models import *
from django.http import *
from django.template.loader import render_to_string
from django.db.models import Q
from datetime import date
# Create your views here.

def index(request):
    context=''
    k=Karyalay.objects.all().order_by('karyalay_name_eglish')
    context={
        'k':k
    }

    return render(request, 'home/index.html',context)



def login(request):
    if request.session.has_key('owner_mobile'):
        return redirect('/owner/owner_dashboard/')
    if 'Login' in request.POST:
        num = request.POST.get('number')
        pin = request.POST.get('pin')
        sunil_login={'mobile':'9730991252','pin':'7878'}
        if sunil_login["mobile"]==num and sunil_login["pin"]==pin:
            request.session['sunil_mobile'] = request.POST.get('number')
            return redirect('/sunil/sunil_dashboard/')
        k= Karyalay.objects.filter(mobile=num,pin=pin,status=1)
        #print(k)
        if k:
            request.session['owner_mobile'] = request.POST.get('number')
            return redirect('/owner/owner_dashboard/')

        else:
            messages.warning(request,"please insert correct information or call more suport 9730991252")
    return render(request, 'home/login.html' )

def karyalay_filter(request):
    if request.method == 'GET':
        words = request.GET['words']
        k=Karyalay.objects.filter(
            Q(karyalay_name_eglish__icontains=words) |
            Q(nearby_location_eglish__icontains=words)| 
            Q(address_eglish__icontains=words) |
            Q(pin_code__icontains=words) |
            Q(owner_name_english__icontains=words) |
            Q(mobile__icontains=words) 
                                  )
        t = render_to_string('ajax/karyalay_filter.html', {'k': k})
        return JsonResponse({'data': t})
    
def karyalay_detail(request,id):
    k=Karyalay.objects.get(id=id)
    i=Images.objects.filter(karyalay_id=id)
    m=Map.objects.filter(karyalay_id=id).first()
    u=You_Tube.objects.filter(karyalay_id=id)
    owner_mobile=''
    if m:
        m=Map.objects.get(karyalay_id=id)
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
    today=date.today()
    e=Event.objects.filter(event_date=today,karyalay_id=id)
    context={
        'k':k,
        'i':i,
        'm':m,
        'owner_mobile':owner_mobile,
        'u':u,
        'e':e,

    }
    return render(request,'home/karyalay_detail.html',context )

def booked_date(request):
    if request.method == 'GET':
        k_id = request.GET['k_id']
        y = request.GET['y']
        m = request.GET['m']
        m=int(m)
        if m < 10:
            m=f'0{m}'
        d=f"{y}-{m}-"
        b=Event.objects.values().filter(event_date__icontains=d,karyalay_id=k_id,status=1)
        book=list(b)
    return JsonResponse({'book':book})


