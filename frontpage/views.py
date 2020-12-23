from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "index.html", context={})


from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = "home.html"
