from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    permissions = models.CharField(blank= True, default="user", max_length=10)
    phone = models.CharField(blank=True, max_length=20)
    pet = models.BooleanField(default=False)
    home = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Device(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mac = models.CharField(max_length=17)
    name = models.CharField(blank=True, max_length=50)
    type = models.CharField(blank=True, max_length=25)
    home = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Log(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    change_date = models.DateTimeField('date changed')
    home = models.BooleanField(default=False)

    def __str__(self):
        return_string = ""
        device = Device.objects.get(id=self.id)
        if self.home:
            return_string = device.name + " - home"
        else:
            return_string = device.name + " - away"
        return return_string