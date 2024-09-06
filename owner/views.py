from django.shortcuts import render ,redirect
from sunil.models import *
from owner.models import *
from camera.models import *
from datetime import datetime, timedelta , date
from django.contrib import messages
# Create your views here.
def owner_dashboard(request):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        context={}
        k=Karyalay.objects.filter(mobile=owner_mobile).first()
        if k:
            k=Karyalay.objects.get(mobile=owner_mobile)
        context={
            'k':k
            }
        return render(request,'owner/owner_dashboard.html',context)
    else:
        return redirect('/login/')


def event(request):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        context={}
        k=Karyalay.objects.filter(mobile=owner_mobile).first()
        if k:
            k=Karyalay.objects.get(mobile=owner_mobile)
            e=Event.objects.filter(karyalay_id=k.id,status=1).order_by('event_date')
        current_time = datetime.datetime.now()
        d = current_time.day -1
        m = current_time.month
        y = current_time.year 
        date_f=f"{y}-{m}-{d}"
        ev = Event.objects.filter(karyalay_id=k.id,event_date__lte=date_f)
        if ev :
            for ev in ev:
                ev.status = 0
                ev.save()
        if 'Add_Event'in request.POST:
            event_name = request.POST.get('event_name')
            parti_name = request.POST.get('parti_name')
            event_date = request.POST.get('event_date')
            if event_date >= str(date.today()):
                Event(
                    karyalay_id=k.id,
                    event_name=event_name,
                    parti_name=parti_name,
                    event_date=event_date,
                    ).save()
                return redirect('/owner/event/')
            else:
                messages.warning(request,"please Select Future Event Day") 
        if 'Edit_Event' in request.POST:
            event_id = request.POST.get('event_id')
            event_name = request.POST.get('event_name')
            parti_name = request.POST.get('parti_name')
            event_date = request.POST.get('event_date')
            if event_date == '' :
                ed = Event.objects.get(id=event_id)
                event_date = ed.event_date
            Event(
                karyalay_id=k.id,
                id = event_id ,
                event_name = event_name ,
                parti_name = parti_name ,
                event_date = event_date ,
                ).save()
            return redirect('/owner/event/')
        context={
            'k':k,
            'e':e
            }
        
        return render(request,'owner/event.html',context)
    else:
        return redirect('/login/')
    

def video(request):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        context={}
        k=Karyalay.objects.filter(mobile=owner_mobile).first()
        u=You_Tube.objects.filter(karyalay_id=k.id)
        if k:
            k=Karyalay.objects.get(mobile=owner_mobile)
        if 'Add_Url' in request.POST:
            url_1 = request.POST.get('url_1')
            url_2 = request.POST.get('url_2')
            You_Tube(
                karyalay_id=k.id,
                url_1=url_1,
                url_2=url_2
                ).save()
            return redirect('/owner/video/')
        elif 'Edit_Url_1' in request.POST:
            url_id = request.POST.get('url_id')
            url_1 = request.POST.get('url_1')
            u_n=You_Tube.objects.get(id=url_id)
            u_n.url_1=url_1
            u_n.save()
            return redirect('/owner/video/')
        elif 'Edit_Url_2' in request.POST:
            url_id = request.POST.get('url_id')
            url_2 = request.POST.get('url_2')
            u_n=You_Tube.objects.get(id=url_id)
            u_n.url_2=url_2
            u_n.save()
            return redirect('/owner/video/')
    
        context={
            'k':k,
            'u':u
            }
        
        return render(request,'owner/video.html',context)
    else:
        return redirect('/login/')


def map(request):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        context={}
        k=Karyalay.objects.filter(mobile=owner_mobile).first()
        if k:
            k=Karyalay.objects.get(mobile=owner_mobile)
        if 'Add_Map_Code'in request.POST:
            map_code = request.POST.get('map_code')
            Map(
                karyalay_id=k.id,
                map_code=map_code
                ).save()
            return redirect('/owner/map/')
    
        context={
            'k':k,
            }
        
        return render(request,'owner/map.html',context)
    else:
        return redirect('/login/')
    

def images(request):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        context={}
        k=Karyalay.objects.filter(mobile=owner_mobile).first()
        if k:
            k=Karyalay.objects.get(mobile=owner_mobile)
            i=Images.objects.filter(karyalay_id=k.id)
            print(i)
        if 'Add_Images'in request.POST:
            image_1 = request.FILES.get("image_1")
            image_2 = request.FILES.get("image_2")
            image_3 = request.FILES.get("image_3")
            image_4 = request.FILES.get("image_4")
            image_5 = request.FILES.get("image_5")
            Images(
                karyalay_id=k.id,
                image_1 = image_1 , 
                image_2 = image_2 ,
                image_3 = image_3 ,
                image_4 = image_4 ,
                image_5 = image_5 ,
            ).save()

            return redirect('/owner/images/')
    
        context={
            'k':k,
            'i':i,
            }
        
        return render(request,'owner/imges.html',context)
    else:
        return redirect('/login/')
    

def profile(request):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        context={}
        k=Karyalay.objects.filter(mobile=owner_mobile).first()
        if k:
            k=Karyalay.objects.get(mobile=owner_mobile)
            if 'edit_profile'in request.POST:
                new_pin = request.POST.get('pin')
                if new_pin:
                    if new_pin != k.pin:
                        k.pin=new_pin
                        k.save()
                        del  request.session['owner_mobile']
                        return redirect('/owner/profile/')
            elif 'show'in request.POST:
                k.booking_show_status = 0
                k.save()
                return redirect('/owner/profile/')
            elif 'hide'in request.POST:
                k.booking_show_status = 1
                k.save()
                return redirect('/owner/profile/')
            elif 'karyalay_show'in request.POST:
                k.show_status = 0
                k.save()
                return redirect('/owner/profile/')
            elif 'karyalay_hide'in request.POST:
                k.show_status = 1
                k.save()
                return redirect('/owner/profile/')
        context={
            'k':k
            }
        return render(request,'owner/profile.html',context)
    else:
        return redirect('/login/')



def lucky_day(request):
    if request.session.has_key('owner_mobile'):
        owner_mobile = request.session['owner_mobile']
        context={}
        k=Karyalay.objects.filter(mobile=owner_mobile).first()
        if k:
            if 'Add_lucky_day'in request.POST:
                form_date = request.POST.get('date')
                today_date = date.today()
                if form_date >= str(today_date) :
                    dt = datetime.strptime(form_date, '%Y-%m-%d').date()
                    if Lucky_day.objects.filter(lucky_day=form_date).exists():
                        messages.warning(request,"Lucky Day Already Exists ") 
                    else:
                        Lucky_day(
                            karyalay_id = k.id,
                            lucky_day = form_date,
                            month = dt.month,
                            year = dt.year,
                            status = 1,
                        ).save()
                        return redirect('/owner/lucky_day/')
                else:
                    messages.warning(request,"please Select Future Lucky Day")            
        context={
            'k':k,
            'lucky_day':Lucky_day.objects.filter(status=1).order_by('lucky_day')
        }
        return render(request, 'owner/lucky_day.html', context)
    else:
        return redirect('login')
    






def woner_logout(request):
    if request.session.has_key('owner_mobile'):
        del  request.session['owner_mobile']
    return redirect('/')