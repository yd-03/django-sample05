from django.shortcuts import render, get_object_or_404
from .forms import UploadForm, SettingForm
from .models import UploadImage


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


def preview(request, image_id=0):
    upload_image = get_object_or_404(UploadImage, id=image_id)

    params = {
        "title": "画像の表示",
        "id": upload_image.id,
        "url": upload_image.image.url,
    }

    return render(request, "upload_app/preview.html", params)


def transform(request, image_id=0):
    upload_image = get_object_or_404(UploadImage, id=image_id)

    if request.method == "POST":
        form = SettingForm(request.POST)
        if form.is_valid():
            angle = form.cleaned_data.get("angle")
            gray = form.cleaned_data.get("gray")
            upload_image.transform(angle, gray)
            params = {
                "title": "画像処理",
                "id": upload_image.id,
                "setting_form": form,
                "original_url": upload_image.image.url,
                "result_url": upload_image.result.url,
            }

            return render(request, "upload_app/transform.html", params)

    params = {
        "title": "画像処理",
        "id": upload_image.id,
        "setting_form": SettingForm({"angle": 0, "gray": False}),
        "original_url": upload_image.image.url,
        "result_url": "",
    }

    return render(request, "upload_app/transform.html", params)
