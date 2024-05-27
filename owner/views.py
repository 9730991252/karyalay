from django.shortcuts import render ,redirect
from sunil.models import *
from owner.models import *
from camera.models import *
from datetime import date
import datetime
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
        return redirect('/login')


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
        date=f"{y}-{m}-{d}"
        ev = Event.objects.filter(karyalay_id=k.id,event_date__lte=date)
        if ev :
            for ev in ev:
                ev.status = 0
                ev.save()
        if 'Add_Event'in request.POST:
            event_name = request.POST.get('event_name')
            parti_name = request.POST.get('parti_name')
            event_date = request.POST.get('event_date')
            Event(
                karyalay_id=k.id,
                event_name=event_name,
                parti_name=parti_name,
                event_date=event_date,
                ).save()
            return redirect('/owner/event/')
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
        return redirect('/login')
    

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
        return redirect('/login')


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
        return redirect('/login')
    

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
        return redirect('/login')
    








def woner_logout(request):
    del  request.session['owner_mobile']
    return redirect('/')