from django.shortcuts import render
from .forms import resumeForm
from .models import resume
from django.views import View

# Create your views here.
class HomeView(View):
    def get(self,request):
        form=resumeForm()
        candidates=resume.objects.all()
        return render(request,'myapp/home.html',{'candidates':candidates,'form':form})
        
    def post(self,request):
        form=resumeForm(request.POST, request.FILES)
        if(form.is_valid()):
            form.save()
            return render(request,'myapp/home.html',{'form':form})

class candidateview(View):
    def get(self,request,pk):
        candidate=resume.objects.get(pk=pk)
        return render(request,'myapp/candidate.html',{'candidate':candidate})