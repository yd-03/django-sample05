from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import LoginForm, SignupForm
from .models import FootPrint


def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(to="/footprints/user/")
    else:
        form = SignupForm()
    param = {"form": form}
    return render(request, "footprints/signup.html", param)


def login_view(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                return redirect(to="/footprints/user/")
    else:
        form = LoginForm()
    param = {"form": form}
    return render(request, "footprints/login.html", param)


def logout_view(request):
    logout(request)
    return redirect(to="/footprints/login/")


@login_required
def user_view(request):
    # ログイン中のユーザーに関連するFootPrintを全て取得し、日付の降順で並べ替える
    footprints = FootPrint.objects.filter(dst=request.user).order_by("-date")
    param = {"user": request.user, "footprints": footprints}
    return render(request, "footprints/user.html", param)


@login_required
def other_view(request, id):
    other = get_object_or_404(User, id=id)
    # ログイン中のユーザーが他のユーザーのページを見たことを記録
    if other != request.user:
        # 以前に同じユーザーのページを見た記録があるか確認
        before_footprints = FootPrint.objects.filter(src=request.user, dst=other)
        if len(before_footprints) == 0:
            # 記録がない場合、新しいFootPrintオブジェクトを作成
            footprint = FootPrint(src=request.user, dst=other)
        else:
            # 記録がある場合、既存のFootPrintオブジェクトの日付を更新
            footprint = before_footprints[0]
            footprint.date = timezone.now()
        # FootPrintオブジェクトを保存して、足跡を記録
        footprint.save()
    # 他のユーザーに関連するFootPrintを全て取得し、日付の降順で並べ替える
    footprints = FootPrint.objects.filter(dst=other).order_by("-date")
    param = {"user": other, "footprints": footprints}
    return render(request, "footprints/other.html", param)


@login_required
def others_view(request):
    others = User.objects.exclude(username=request.user.username)
    param = {"others": others}
    return render(request, "footprints/others.html", param)
