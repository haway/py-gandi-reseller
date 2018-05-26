from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

import configs.config as cfg
from Contacts.models import Contact
from Domains.models import Domain

from Domains.views import getTLDs
from Domains.views import getTLDsPrice

# Create your views here.

@login_required

def home(request):

    uname = request.user.username
    Contacts = Contact.objects.filter(user=request.user)
    Domains = Domain.objects.filter(user=request.user)
    TLDs = getTLDs()
    DEBUG = "Hi debug guy"

    return render(request, 'home.html', {
            'username': uname,
            'Contacts_list': Contacts,
            'Domains_list': Domains,
            'TLDs': TLDs,
            'DEBUG': DEBUG,
        } )


    

