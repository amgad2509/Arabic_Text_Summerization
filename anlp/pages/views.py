from django.shortcuts import render
#from django.http import HttpResponse
from .utils import get_summary , tokenizer , device , model_nlp

# Create your views here.
def index(request):
    #return HttpResponse('hello')
    return render(request, 'index.html')
def home(request):
   return render(request, 'home.html')
def model(request):
    if request.method == "POST":
        text = request.POST["text"]
        summary = get_summary(text, tokenizer, model_nlp, device)
        return render(request, "model.html", {"summary": summary})
    else:
        return render(request, "model.html")
