from django.shortcuts import render

# Create your views here.
def getIndex(request):
    return render(request, 'practice/index.html')