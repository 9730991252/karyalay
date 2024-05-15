from django.shortcuts import render ,redirect
from sunil.models import *
from owner.models import *

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
            e=Event.objects.filter().order_by('event_date')
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
            return redirect('/owner/event')
    
        context={
            'k':k,
            'e':e
            }
        
        return render(request,'owner/event.html',context)
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

            return redirect('/owner/images')
    
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