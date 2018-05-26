from django.shortcuts import render
from Domains.models import Domain
from django.http import JsonResponse

import math
import time
import configs.config as cfg
from Contacts.views import getContactCTID

# Create your views here.

def DNInfo(fqdn):
    DNData = cfg.gapi.domain.info( cfg.APIKEY, fqdn );
    return DNData

def DNDetail(request, fqdn):
    DNData = DNInfo( fqdn ) 
    zone_id = DNData['zone_id']
    Records = cfg.gapi.domain.zone.record.list( cfg.APIKEY, zone_id, 0 );

    return render(request, "DNDetail.html", {
                    'fqdn': fqdn,
                    'DNData': DNData,
                    'Records': Records,
                    }
                 )

def rawTLDlist(spec = { 'product':{'type': 'domains'}, 'action':{ 'name': 'create' } } ):
    rtlds = cfg.gapi.catalog.list( cfg.APIKEY, spec )
    return rtlds


def getTLDs():
    tlds = []
    rawtlds = rawTLDlist()
    for domain in rawtlds:
        tlds.append( domain['product']['description'] )

    return tlds

def getTLDsPrice():
    tlds = []
    rawtlds = rawTLDlist()
    for domain in rawtlds:
        strtmp = domain['product']['description'] + " ( $" + str(math.ceil(domain['unit_price'][0]['price'] * 35)) + " )"
        tlds.append(strtmp)

    return tlds

def getDNQuery(fqdn):       # internal
    # Domain check

    result = cfg.gapi.domain.available( cfg.APIKEY, [fqdn] );
    while result[fqdn] == 'pending':
        time.sleep(0.7)
        result = cfg.gapi.domain.available( cfg.APIKEY, [fqdn] );

    return result;


def DNQuery(request, fqdn):
    result = getDNQuery( fqdn );

    return render(request, "DNQuery.html", {
                    'fqdn': fqdn,
                    'status': result[fqdn],
                 })

def jDNQuery(request, fqdn):
    result = getDNQuery( fqdn );

    return JsonResponse( result );

def getAssocCheck( fqdn, ctid, fo, fa, ft, fb ):

    as_spec = {
            'domain': fqdn,
            'owner': fo,
            'admin': fa,
            'bill': fb,
            'tech': ft }

    result = cfg.gapi.contact.can_associate_domain( cfg.APIKEY, ctid )

    return result

def preDNCreate(request, fqdn):

    ctid = getContactCTID( request )
    return render( request, "preDNCreate.html", {
                'fqdn': fqdn,
                'ctid': ctid,
        })


def DNCreate(request):

    fqdn = request.GET.get('fqdn', '')
    owner = request.GET.get('owner', '')
    admin = request.GET.get('admin', '')
    tech = request.GET.get('tech', '')
    bill = request.GET.get('bill', '')
    duration = int( request.GET.get('duration','') )

    contacts_ok = True
    nameservers_ok = False
    status = "start process"

    #ctid = getContactCTID( request )
    #DEBUG = "<br>citd:"+ctid

    if not getAssocCheck( fqdn, owner, True, False, False, False ):
        status += ",Owner Assocation check failed"
        contacts_ok = False

    if not getAssocCheck( fqdn, admin, False, True, False, False ):
        status += ",Admin Assocation check failed"
        contacts_ok = False

    if not getAssocCheck( fqdn, tech, False, False, True, False ):
        status += ",Tech Assocation check failed"
        contacts_ok = False

    if not getAssocCheck( fqdn, bill, False, False, False, True ):
        status += ",Bill Assocation check failed"
        contacts_ok = False

    status += "Contacts_ok:" + str( contacts_ok )

    if contacts_ok :
        domain_spec = {
                'owner': owner,
                'admin': admin,
                'bill': bill,
                'tech': tech,
                'duration': duration }

        op = cfg.gapi.domain.create( cfg.APIKEY, fqdn, domain_spec )
        status += ",process id: "+str(op['id'])+", STEP:"+op['step']
        if op['step'] == 'DONE':
            status = "OK! Register successly"
            Domain.objects.create(user=request.user, fqdn=fqdn, dnstatus='ok')
        else:
            dcount = 5
            while op['step'] != 'DONE' and dcount > 0:
                op = cfg.gapi.operation.info( cfg.APIKEY, op['id'] )
                time.sleep(1.0)
                dcount -= 1

            Domain.objects.create(user=request.user, fqdn=fqdn, dnstatus=op['step'] )

    else:
        status += ", Failed"

    return render( request, "DNCreate.html", {
                'fqdn': fqdn,
                'status': status,
        })

