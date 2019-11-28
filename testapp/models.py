from django.db import models

# Varibles we want to work on are defined here and later migrated in sqldatabase using sql commands
class data(models.Model):
    visitorname = models.CharField(max_length=100, blank=False,)
    visitoremail = models.EmailField(max_length=140, blank=False)
    visitorphone = models.CharField(max_length=10, blank=False)
    hostname = models.CharField(max_length=100, blank=False)
    hostemail = models.EmailField(max_length=40, blank=False)
    hostphone = models.CharField(max_length=10, blank=False)
    visitorarrivaltime = models.TimeField(auto_now_add=True)
    visitordeparturetime = models.TimeField(auto_now=True)
    addressvisited =models.CharField(max_length=100,default="The LNMIIT Institute Of Information Technology,Jaipur")
    departed = models.BooleanField(default=False)

    def __str__(self):
        return self.visitorname

