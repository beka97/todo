from django.shortcuts import render, HttpResponse

def homepage(request):
    return HttpResponse("hello word!")

def test(request):
    return render(request, "test.html")