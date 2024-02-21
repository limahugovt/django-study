from django.shortcuts import render

def ViewLogin(request):
    return render(request, 'login.html')
