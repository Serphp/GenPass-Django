from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import *
from .utils import generate_password


# Create your views here.
def error_404_view(request, exception):
    return render(request, "404.html")


def myfunctioncall(request):
    return render(request, "index.html")


def gp(request):
    length = int(request.GET.get("length", 16))
    include_uppercase = request.GET.get("uppercase"), True
    include_numbers = request.GET.get("numbers"), True
    password = generate_password(length, include_uppercase, include_numbers)
    mydictionary = {"password": password}
    return render(request, "index.html", context=mydictionary)


def myfunctionabout(request):
    return HttpResponse("About Response")


def add(request, a, b):
    return HttpResponse(a + b)


def intro(request, name, age):
    mydictionary = {"name": name, "age": age}
    return JsonResponse(mydictionary)


def myimagepage5(request, imagename):
    myimagename = str(imagename)
    myimagename = myimagename.lower()
    print(myimagename)
    if myimagename == "django":
        var = True
    elif myimagename == "python":
        var = False
    mydictionary = {"var": var}
    return render(request, "imagepage5.html", context=mydictionary)


def myform(request):
    return render(request, "myform.html")


def submitmyform(request):
    mydictionary = {
        "var1": request.POST["mytext"],
        "var2": request.POST["mytextarea"],
        "method": request.method,
    }
    return JsonResponse(mydictionary)


def myform2(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            title = request.POST["title"]
            subject = request.POST["subject"]
            email = request.POST["email"]
            mydictionary = {"form": FeedbackForm()}
            errorflag = False
            Errors = []
            if title != title.upper():
                errorflag = True
                errormsg = "Title should be in Capital"
                Errors.append(errormsg)
            import re

            regex = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"
            if not re.search(regex, email):
                errorflag = True
                errormsg = "Not a Valid Email address"
                Errors.append(errormsg)
            if errorflag != True:
                mydictionary["success"] = True
                mydictionary["successmsg"] = "Form Submitted"
            mydictionary["error"] = errorflag
            mydictionary["errors"] = Errors
            print(mydictionary)
            return render(request, "myform2.html", context=mydictionary)

    elif request.method == "GET":
        form = FeedbackForm()  # FeedbackForm(None)
        mydictionary = {"form": form}
        return render(request, "myform2.html", context=mydictionary)
