from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Domain(models.Model):
    user = models.ForeignKey(
                User,
                related_name='domains',
                on_delete = models.CASCADE
            )
    fqdn = models.CharField(max_length=128)
    dnstatus = models.CharField(max_length=20)

    #Owner = models.CharField(max_length=20)
    #Admin = modles.CharField(max_length=20)
    #Tech = models.CharField(max_length=20)
    #Bill = models.CharField(max_length=20)
    #NameServers = models.
    #ExpireDate 
    #Duration = models.
    #CreateDate
    #RenewDate
    #AddPeriod
    #AutoRenewPeriod
    #Inactive
    #OK
    #PendingCreate
    #PendingDelete
    #PendingRenew
    #PendingRestore 
    #PendingTransfer
    #PendingUpdate
    #RedemptionPeriod
    #RenewPeriod
    #ServerDeleteProhibited
    #ServerHold
    #ServerRenewProhibited
    #ServerTransferProhibited
    #ServerUpdateProhibited
    #TransferPeriod



