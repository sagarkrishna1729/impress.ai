from django.db import models
from django.contrib.auth.models import User

class ButtonCall(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True )
    button = models.CharField(max_length=20)
    call_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user},{self.button}"