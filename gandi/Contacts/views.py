from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

import configs.config as cfg
from Contacts.models import Contact


# Create your views here.
def CTInfo(CTID):
    CTData = cfg.gapi.contact.info( cfg.APIKEY, CTID )

    return CTData


def CTDetail(request, ctid):

    CTData = CTInfo( ctid )

    return render(request, "CTDetail.html", {
                'CTID': ctid,
                'CTDATA': CTData,
                }
           )

def getContactCTID(request):
    
     obj = Contact.objects.filter(user=request.user)

     return obj[0].ctid
     


