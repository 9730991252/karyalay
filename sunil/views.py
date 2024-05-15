from django.shortcuts import render, redirect
from sunil.models import *
from django.contrib import messages 
# Create your views here.

def sunil_dashboard(request):
   
    return render(request,'sunil/sunil_dashboard.html')


def add_karyalay(request):
    context={}
    k=Karyalay.objects.all()
    if 'Add_New_Karyalay' in request.POST:
        karyalay_name_marathi = request.POST.get('karyalay_name_marathi')
        karyalay_name_eglish = request.POST.get('karyalay_name_eglish')
        nearby_location_marathi = request.POST.get('nearby_location_marathi')
        nearby_location_eglish = request.POST.get('nearby_location_eglish')
        address_marathi = request.POST.get('address_marathi')
        address_eglish = request.POST.get('address_eglish')
        pin_code = request.POST.get('pin_code')
        owner_name_marathi = request.POST.get('owner_name_marathi')
        owner_name_english = request.POST.get('owner_name_english')
        mobile = request.POST.get('mobile')
        pin = request.POST.get('pin')
        if Karyalay.objects.filter(mobile=mobile).exists():
            messages.warning(request,"Owner Mobile Allready Exists")
        else : 
            Karyalay(
                karyalay_name_marathi = karyalay_name_marathi ,
                karyalay_name_eglish = karyalay_name_eglish ,
                nearby_location_marathi = nearby_location_marathi ,
                nearby_location_eglish = nearby_location_eglish ,
                address_marathi = address_marathi ,
                pin_code=pin_code,
                address_eglish = address_eglish ,
                owner_name_marathi = owner_name_marathi ,
                owner_name_english = owner_name_english ,
                mobile = mobile ,
                pin = pin ,
                ).save()
            return redirect('add_karyalay')
    if 'Edit_Karyalay' in request.POST:
        karyalay_id = request.POST.get('karyalay_id')
        karyalay_name_marathi = request.POST.get('karyalay_name_marathi')
        karyalay_name_eglish = request.POST.get('karyalay_name_eglish')
        nearby_location_marathi = request.POST.get('nearby_location_marathi')
        nearby_location_eglish = request.POST.get('nearby_location_eglish')
        address_marathi = request.POST.get('address_marathi')
        address_eglish = request.POST.get('address_eglish')
        pin_code = request.POST.get('pin_code')
        owner_name_marathi = request.POST.get('owner_name_marathi')
        owner_name_english = request.POST.get('owner_name_english')
        mobile = request.POST.get('mobile')
        pin = request.POST.get('pin')
        Karyalay(
            id = karyalay_id ,
            karyalay_name_marathi = karyalay_name_marathi ,
            karyalay_name_eglish = karyalay_name_eglish ,
            nearby_location_marathi = nearby_location_marathi ,
            nearby_location_eglish = nearby_location_eglish ,
            address_marathi = address_marathi ,
            pin_code=pin_code,
            address_eglish = address_eglish ,
            owner_name_marathi = owner_name_marathi ,
            owner_name_english = owner_name_english ,
            mobile = mobile ,
            pin = pin ,
                ).save()
        return redirect('add_karyalay')
    context={
        'k':k
    }
    return render(request,'sunil/add_karyalay.html',context)