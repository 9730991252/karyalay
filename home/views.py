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
    test(request)
    context=''
    k=Karyalay.objects.filter(show_status=1,status=1).order_by('karyalay_name_eglish')
    context={
        'k':k
    }
    return render(request, 'home/index.html',context)

def contact_us(request):
    return render(request, 'home/contact_us.html')
def about_us(request):
    return render(request, 'home/about_us.html')

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
    k=Karyalay.objects.get(id=id,show_status=1,status=1)
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
        b=Event.objects.values().filter(event_date__icontains=d,karyalay_id=k_id)
        book=list(b)
    return JsonResponse({'book':book})



def check_date(request):
    if request.method == 'GET':
        k_id = request.GET['k_id']
        k=Karyalay.objects.get(id=k_id)
        y = request.GET['y']
        m = request.GET['m']
        d = request.GET['d']
        d=int(d)
        m=int(m)
        if m < 10:
            m=f'0{m}'
        if d < 10:
            d=f'0{d}'
        d=f"{y}-{m}-{d}"
        e=Event.objects.values().filter(event_date=d,karyalay_id=k_id)
        print(e)
        context={
            'k':k,
            'e':e,
            'd':d
        }
        t = render_to_string('ajax/check_event.html', context)
    return JsonResponse({'data': t})


def test(request):
    q='s'
    a=Event.objects.filter(karyalay__karyalay_name_eglish__icontains=q)
 
    print(a)