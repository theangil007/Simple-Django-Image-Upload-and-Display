from django.shortcuts import render, redirect
from .models import fileupload

# Create your views here.


def homepage_view(request):
    if request.method == "POST":
        imagename = request.POST.get("imagename")
        imagefile = request.FILES.get("imagefile")

        user = fileupload.objects.create(Imagename=imagename, Imagefile=imagefile)
        message = "Image has been successfully uploaded."
        return render(request, "index.html", {"msg": message})
    else:
        return render(request, "index.html")


# Image Fetching View
def ImageFetch(request):
    all_img = fileupload.objects.all()
    return render(request, "index.html", {"all_img": all_img})
