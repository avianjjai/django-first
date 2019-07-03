from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from .forms import UserForm,UserProfileInfoForm,CreateSortCode
from .models import Bitly
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def index(request):
    import json
    shortcodes = Bitly.objects.filter(username__iexact=request.user.username)[::-1]
    clicks = {}
    for x in shortcodes:
        instance = json.loads(x.datewise)
        clicks[x] = sum(instance.values())
    return render(request,'index.html',{'shortcodes':shortcodes,'clicks':clicks,'total_clicks':sum(clicks.values()),'len':len(shortcodes)})

def signup(request):
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            if user_form.data['password']==profile_form.data['con_password']:
                print(profile_form.data['con_password'])
                user_name = user.email[:user.email.index('@')]
                user.username = user_name
                user.set_password(user.password)
                user.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()

    return HttpResponseRedirect(reverse('short:index'))

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_name = email[:email.index('@')]
        user = authenticate(username=user_name,password=password)
        if user:
            if user.is_active:
                login(request,user)
    return HttpResponseRedirect(reverse('short:index'))

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('short:index'))

def shorturl(request):
    from .utils import create_Sortcode,gettitle
    if request.method == 'POST':
        user_name = request.user.username
        form = CreateSortCode(data=request.POST)
        import json
        instance = form.save(commit=False)
        instance.shortcode = create_Sortcode()
        instance.datewise = json.dumps({})
        instance.username = user_name
        instance.title = gettitle(instance.long_url)
        instance.save()
    return HttpResponseRedirect(reverse('short:index'))

def detail(request,id):
    shortcode = Bitly.objects.filter(id__iexact=id)[::-1]
    return render(request,'page2.html',{'shortcode':shortcode[0]})


def goto(request,shortcode):
    import json
    import datetime
    qs = get_object_or_404(Bitly,shortcode__iexact = shortcode)
    if qs:
        today = datetime.datetime.now().date()
        instance = json.loads(qs.datewise)
        if str(today) in instance:
            instance[str(today)] += 1
        else:
            instance[str(today)] = 1
        qs.datewise = json.dumps(instance)
        qs.save()
    return HttpResponseRedirect(qs.long_url) 

def delete(request,id):
    if request.user.is_authenticated:
        qs = get_object_or_404(Bitly,id =id)
        if qs and request.user.username == qs.username:
            qs.delete()
    return HttpResponseRedirect(reverse('short:index'))




