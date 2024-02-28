from django.shortcuts import redirect, render

from .forms import FormRegister


def register(response):
    if response.method == "POST":
        form = FormRegister(response.POST)
        if form.is_valid():
            form.save()
            return redirect("auth/login")

    else:
        form = FormRegister()
    return render(response, "register.html", {"register": form})
