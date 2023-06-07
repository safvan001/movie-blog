from django.shortcuts import render
from movieblogger.models import movie
from movieblogger.forms import movieform
from django.views.generic import ListView,DetailView,CreateView
from django.urls import reverse_lazy

'''

def base(request):
    m=movie.objects.all()
    return render(request,'base.html',{'m':m})
'''
class MovieListView(ListView):
    model=movie
    template_name="base.html"
    context_object_name ="m"
    '''
    def veiw(request,p):
        b=movie.objects.get(id=p)
        return render(request,'movieveiw.html',{'movie':b})
    '''


class MovieDetailView(DetailView):
    model=movie
    template_name="movieveiw.html"
    context_object_name='movie'

def update(request,p):
    b = movie.objects.get(id=p)
    f=movieform(instance=b) #create empty form object
    if (request.method=="POST"):
        print(request.POST) #used to print entered values in terminal
        f=movieform(request.POST,request.FILES,instance=b) #create form object using values received from form
                                 #request.POST-dictionary sent from template

        if(f.is_valid()):
            f.save()
        return base(request)
    return render(request,'edit.html',{'form':f})
'''
def add(request):
    form=movieform()
    if(request.method == "POST"):
        print(request.POST)  # used to print entered values in terminal
        form = movieform(request.POST,request.FILES)
        if (form.is_valid()):
            form.save()
            return base(request)
    return render(request,'add.html',{'movie':form})
'''
class MovieaddView(CreateView):
    model=movie
    template_name='add.html'
    fields=['name','desc','img']
    success_url = reverse_lazy('movieblogger:base')

def delete(request,p):
    b=movie.objects.get(id=p)
    b.delete()
    return base(request)


# Create your views here.
