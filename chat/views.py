import os
from chat.models import Chat, Volunteer, Patient, Nurse
import speech_recognition as sr
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
from textblob import TextBlob
from django.http import HttpResponse, HttpResponseRedirect

from .models import Volunteer, Nurse
from json import dumps
import datetime
from django.shortcuts import get_list_or_404, get_object_or_404
from django.shortcuts import render, redirect
# from .forms import OrderForm,InterestForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import io
import urllib, base64


def home(request):
    chats = Chat.objects.all()
    all_users = User.objects.filter(messages__isnull=False).distinct()
    ctx = {
        'home': 'active',
        'chat': chats,
        'allusers': all_users
    }
    if request.user.is_authenticated:
        return render(request, 'chat.html', ctx)
    else:
        return render(request, 'base.html', None)


def upload(request):
    customHeader = request.META['HTTP_MYCUSTOMHEADER']

    # obviously handle correct naming of the file and place it somewhere like media/uploads/
    filename = str(Chat.objects.count())
    filename = filename + "name" + ".wav"
    uploadedFile = open(filename, "wb")
    # the actual file is in request.body
    uploadedFile.write(request.body)
    uploadedFile.close()
    # put additional logic like creating a model instance or something like this here
    r = sr.Recognizer()
    harvard = sr.AudioFile(filename)
    with harvard as source:
        audio = r.record(source)
    msg = r.recognize_google(audio)
    os.remove(filename)
    sent = TextBlob(msg)
    chat_message = Chat(user=request.user, message=msg, subjectivity=sent.subjectivity, polarity=sent.polarity)

    # Adarshg

    if msg != '':
        chat_message.save()
    return redirect('/')


def post(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        print('Our value = ', msg)
        chat_message = Chat(user=request.user, message=msg)
        if msg != '':
            chat_message.save()
        return JsonResponse({'msg': msg, 'user': chat_message.user.username})
    else:
        return HttpResponse('Request should be POST.')


def messages(request, user_name):
    chat = Chat.objects.all()
    polarity = Chat.objects.values_list('polarity', flat=True).filter(user=user_name)
    subjectivity = Chat.objects.values_list('subjectivity', flat=True)
    # subjectivity=subjectivity.filter(subjectivity!="NA")
    plt.xlabel('Sentence numbers')
    plt.ylabel('Polarity Value')
    plt.plot(polarity)
    fig = plt.gcf()
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    string = base64.b64encode(buf.read())
    uri = urllib.parse.quote(string)

    return render(request, 'messages.html', {'chat': chat, 'data': uri})


# def sentiment_analysis(request):

def heart_Ml_Pred(request):
    return render(request, 'Heart_Disease_Prediction.html')


def patient_page(request,user_id):
    patient = Patient.objects.all().filter(pat_id=user_id)
    print(patient[0].pat_id)
    return render(request, 'Patient1.html', {'patient': patient})
def volunteer_page(request,user_id):
    volunteer=Volunteer.objects.all().filter(vol_id=user_id)
    return render(request,'Volunteer.html',{'volunteer':volunteer})
def nurse_page(request,user_id):
    nurse=Nurse.objects.all().filter(nurse_id=user_id)
    return render(request,'Nurse.html',{'nurse':nurse})
