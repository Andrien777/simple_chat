import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Message
from .utils import *


# Create your views here.
def main(request):
    messages = Message.objects.order_by("time").all()
    context = {'messages': messages, 'ip': get_client_ip(request)}
    return render(request, 'index.html', context)


def new(request):
    new_text = request.POST['text']
    new_text = new_text.strip(' ')
    new_text = wordfilter(new_text)
    ip = get_client_ip(request)
    msg = Message(text=new_text, from_user=ip, time=datetime.datetime.now())
    msg.save()
    return HttpResponseRedirect(reverse("main"))
