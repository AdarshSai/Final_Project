import base64
import io
import os
import json
import urllib
import matplotlib.pyplot as plt
import speech_recognition as sr
# from .forms import OrderForm,InterestForm, RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.serializers import json
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from textblob import TextBlob
import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string

from .forms import PatientRegisterForm, VolunteerRegisterForm
from .models import Volunteer, Nurse,Chat,health_habbits,Patient


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


def patient_page(request, user_id):
    patient = Patient.objects.all().filter(pat_id=user_id)
    health_details=health_habbits.objects.all().filter(hid=user_id)
    print(patient[0].pat_id)
    return render(request, 'Patient1.html', {'patient': patient,'health':health_details})


def volunteer_page(request, user_id):
    volunteer = Volunteer.objects.all().filter(vol_id=user_id)
    return render(request, 'Volunteer.html', {'volunteer': volunteer})


def nurse_page(request, user_id):
    nurse = Nurse.objects.all().filter(nurse_id=user_id)
    return render(request, 'Nurse.html', {'nurse': nurse})


def question_ans(request):
    import json
    datalist = []
    with open(r'C:\Users\Adarsh\Documents\portfolio-project\prac.txt') as data_file:
        for jsonObj in data_file:
            # print(jsonObj)
            data = json.loads(jsonObj)
            datalist.append(data)
    for student in datalist:
        print(student["tags"], student["answer"], student["answer_author"], student["question"],
              student["question_text"])

    return render(request, 'account/question_ans.html', {'data_list': datalist})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('chat:base'))
                else:
                    return HttpResponse('Your account is disabled.')
            else:
                return HttpResponse('Invalid login details.')
        else:
            return HttpResponse("Please enable cookies to continue")
    else:
        request.session.set_test_cookie()
        return render(request, 'login.html')


@login_required(login_url='chat:login')
def user_logout(request):
    request.session.clear()
    return HttpResponseRedirect(reverse('chat:base'))


def registerpatient(request):
    if request.method == 'POST':
        form = PatientRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            patient = form.save(commit=False)
            patient.set_password(patient.password)
            patient.save()
            msg = ' Patient registration successfully.'
            return render(request, 'message.html', {'msg': msg})
    else:
        form = PatientRegisterForm()
    return render(request, 'registration/registerPatient.html', {'form': form})


def registervolunteer(request):
    if request.method == 'POST':
        form = VolunteerRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            volunteer = form.save(commit=False)
            volunteer.set_password(volunteer.password)
            volunteer.save()
            msg = ' volunteer registration successfully.'
            return render(request, 'message.html', {'msg': msg})
    else:
        form = VolunteerRegisterForm()
    return render(request, 'registration/registerVolunteer.html', {'form': form})


def register(request):
    return render(request, 'registration/register.html')


def base(request):
    return render(request, 'base.html')


def about(request):
    return render(request, 'about_us1.html')


def load_json_table_format(request):
    with open(r'C:\Users\neera\Desktop\Final_Project\templates\bot\New_one.json', 'r', encoding='utf-8') as data_file:    
        data = json.load(data_file)
    # pprint(data)
   # html = render_to_string()
    return render(request,'faq.html', {"d":data})
    #return HttpResponse({'d':data}, 'faq.html', content_type="application/html")