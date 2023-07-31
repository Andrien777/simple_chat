from django.db import models


# Create your models here.
class Message(models.Model):
    time = models.DateTimeField(auto_created=True, default=0)
    from_user = models.CharField(default='127.0.0.1', max_length=15)
    text = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.from_user}: {self.text}"
