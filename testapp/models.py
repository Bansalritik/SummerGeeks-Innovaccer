from django.db import models
from django.core.validators import RegexValidator
phone_regex = RegexValidator(regex=r'^\+?1?\d{10,15}$',
                             message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.")


# Varibles we want to work on are defined here and later migrated in sqldatabase using sql commands
class data(models.Model):
    visitorname = models.CharField(max_length=100, blank=False,)
    visitoremail = models.EmailField(max_length=140, blank=False)
    visitorphone = models.CharField(validators=[phone_regex], max_length=10, blank=False)
    hostname = models.CharField(max_length=100, blank=False)
    hostemail = models.EmailField(max_length=40, blank=False)
    hostphone = models.CharField(validators=[phone_regex], max_length=10, blank=False)
    visitorarrivaltime = models.TimeField(auto_now_add=True)
    visitordeparturetime = models.TimeField(auto_now=True)
    addressvisited =models.CharField(max_length=100,default="The LNMIIT Institute Of Information Technology,Jaipur")
    departed = models.BooleanField(default=False)

    def __str__(self):
        return self.visitorname

