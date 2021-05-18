from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class GM(models.Model):
    user = User()
    
    cap_space = models.IntegerField()
    cap_slots = models.SmallIntegerField()
    
    has_used_to = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.user.last_name}, {self.user.first_name}: {self.user.username}'

class FreeAgent(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    image = models.URLField(null=True)
    
    is_rfa = models.BooleanField(default=False)
    rfa_owner = GM()
    
    last_bid = models.IntegerField()
    last_bid_time = models.DateTimeField(auto_now=True)
    last_bid_owner = GM()
    
    fpg = models.FloatField(null=True)
    
    bid_has_ended = models.BooleanField(default=False)