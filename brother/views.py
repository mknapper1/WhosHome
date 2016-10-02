from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from django.urls import reverse

# Create your views here.
from .models import User, Device, Log

class all_family(generic.ListView):
    template_name = 'brother/all_family.html'
    context_object_name = 'all_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return User.objects.all().order_by('-name')

class all_home(generic.ListView):
    template_name = 'brother/all_home.html'
    context_object_name = 'all_home_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return User.objects.filter(
            home=True
        ).order_by('-name')

class all_not_home(generic.ListView):
    template_name = 'brother/all_not_home.html'
    context_object_name = 'all_not_home_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return User.objects.filter(
            home=False
        ).order_by('-name')

def checking_in(request, mac_address):
    device = Device.objects.get(mac=mac_address)
    device.home = True
    device.save()
    user = User.objects.get(id=device.user_id)
    user.home = True
    user.save()
    log = Log(device_id=device.id, home=True, change_date=timezone.now())
    log.save()
    return HttpResponse("Success!")

def checking_out(request, mac_address):
    device = Device.objects.get(mac=mac_address)
    device.home = False
    device.save()
    user = User.objects.get(id=device.user_id)
    if device.type == "phone":
        user.home = False
        user.save()
    if user.pet:
        user.home = False
        user.save()
    log = Log(device_id=device.id, home=False, change_date=timezone.now())
    log.save()
    return HttpResponse("Success!")