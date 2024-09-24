from django.shortcuts import render
from .forms import UploadForm


def index(request):
    params = {
        "title": "画像のアップロード",
        "upload_form": UploadForm(),
        "id": None,
    }
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            upload_image = form.save()
            params["id"] = upload_image.id
    return render(request, "upload_app/index.html", params)
