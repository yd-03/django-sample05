from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class FootPrint(models.Model):
    src = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="src_footprint"
    )
    dst = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="dst_footprint"
    )
    date = models.DateTimeField(default=timezone.now)
