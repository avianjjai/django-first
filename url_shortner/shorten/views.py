from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
from .models import bitly
from .forms import bitlyForm,editBitly

def index(request):
    objects = bitly.objects.all()
    print(objects)
    context = {'objs':objects}
    return render(request,'index.html',context)

def create(request):
    from .utils import create_Sortcode
    form = bitlyForm(request.POST or None)
    if form.is_valid():
        import json
        instance = form.save(commit = False)
        instance.shortcode = create_Sortcode()
        instance.datewise = json.dumps({})
        instance.save()

        return HttpResponseRedirect("http://127.0.0.1:8000/home/")

    context = {"urlform":form}
    return render(request,"create.html",context)

def goto(request,shortcode = None):
    import json
    import datetime
    qs = get_object_or_404(bitly,shortcode__iexact = shortcode)
    if qs:
        today = datetime.datetime.now().date()
        instance = json.loads(qs.datewise)
        if str(today) in instance:
            instance[str(today)]+=1
        else:
            instance[str(today)]= 1
        qs.datewise = json.dumps(instance)
        qs.save()      
    return HttpResponseRedirect(qs.long_url)

def update(request,pk = None):
    qs = get_object_or_404(bitly, id = pk)
    form = editBitly(request.POST or None, instance=qs)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("http://127.0.0.1:8000/home")

    context = {'urlform':form}
    return render(request,"create.html",context)

def delete(request,pk = None):
    qs = get_object_or_404(bitly,id = pk)
    qs.delete()
    return HttpResponseRedirect("http://127.0.0.1:8000/home")