from django.shortcuts import render, reverse
from myapp.forms import FeedbackForm
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    return render(request,'javascript.html')

def home(request):
    return render(request,'index.html')


def history(request):
    return render(request, 'history.html')

def project(request):
    return render(request, 'project.html')

def research(request):
    return render(request, 'research.html')

def overview(request):
    return render(request,'overview.html')
def contact(request):
    form = FeedbackForm()

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save(commit = True)
            print('data added Successfully!!!')
            return HttpResponseRedirect(reverse('index'))
    return render(request,'feedback.html',{'form':form})
