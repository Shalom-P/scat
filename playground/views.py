from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Newcat,Newslearnbbc,Newslearneuronews,Newslearnwion
from .forms import Newcatform
from .getnews import gnews

# Create your views here.

def add_sentence(request):
    submitted = False
    if request.method == "POST":
        form = Newcatform(request.POST)
        if form.is_valid():
            form.save()
            data_from_youtube(request.POST['sentence'])
            ##data_from_youtube()
            return HttpResponseRedirect('/as?submitted=True')
        else:
            form = Newcatform
            if 'submitted' in request.GET:
                submitted = True
    form = Newcatform
    return render(request,'forms.html',{'form':form,'submitted':submitted})

def get_the_sentence(request):
    listt = Newcat.objects.all()
    return render(request,'index.html',
    {'listt':listt})

def data_from_youtube(sentence):
    wion,bbc,euronews = gnews(sentence)
    entrywion = Newslearnwion(sent = sentence,title1=wion[0]['title'],link1=wion[0]['channel']['channel_link'],title2=wion[1]['title'],link2=wion[1]['channel']['channel_link'],title3=wion[2]['title'],link3=wion[2]['channel']['channel_link'],title4=wion[3]['title'],link4=wion[3]['channel']['channel_link'],title5=wion[3]['title'],link5=wion[3]['channel']['channel_link'])
    entrywion.save()
    entrybbc = Newslearnbbc(sent = sentence,title1=bbc[0]['title'],link1=bbc[0]['channel']['channel_link'],title2=bbc[1]['title'],link2=bbc[1]['channel']['channel_link'],title3=bbc[2]['title'],link3=bbc[2]['channel']['channel_link'],title4=bbc[3]['title'],link4=bbc[3]['channel']['channel_link'],title5=bbc[3]['title'],link5=bbc[3]['channel']['channel_link'])
    entrybbc.save()
    entryeuronews = Newslearneuronews(sent = sentence,title1=euronews[0]['title'],link1=euronews[0]['channel']['channel_link'],title2=euronews[1]['title'],link2=euronews[1]['channel']['channel_link'],title3=euronews[2]['title'],link3=euronews[2]['channel']['channel_link'],title4=euronews[3]['title'],link4=euronews[3]['channel']['channel_link'],title5=euronews[3]['title'],link5=euronews[3]['channel']['channel_link'])
    entryeuronews.save()