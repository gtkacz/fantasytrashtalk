from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import post_save
from django.dispatch import receiver
from countdowntimer_model.models import CountdownTimer

# Create your models here.

class GM(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    email_confirmed = models.BooleanField(default=False)
    
    cap_space = models.IntegerField()
    cap_slots = models.SmallIntegerField()
    
    has_used_to = models.BooleanField(default=False)
    
    # user_bids = ArrayField(base_field=models.ForeignKey('FreeAgent', on_delete=models.CASCADE), size=cap_slots)
    
    def __str__(self):
        return f'{self.user.last_name}, {self.user.first_name}: {self.user.username}'
    
class BidCountdown(CountdownTimer):
    pass
    
class Bid(models.Model):
    last_bid = models.IntegerField()
    last_bid_time = models.DateTimeField()
    last_bid_owner = models.ForeignKey(GM, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.id} : {self.last_bid_owner.username} bid {self.last_bid} on {self.auctionListing.name} at {self.last_bid_time}"

class FreeAgent(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    image = models.URLField(null=True)
    
    is_rfa = models.BooleanField(default=False)
    rfa_owner = models.ForeignKey(GM, on_delete=models.CASCADE, default=None)
    
    last_bid = models.ForeignKey(Bid, on_delete=models.CASCADE)
    
    fpg = models.FloatField(null=True)
    
    bid_has_ended = models.BooleanField(default=False)
    
    # position = ArrayField(base_field=models.CharField(max_length=3, null=True), null=True)
    position = models.CharField(max_length=12, null=True)
    
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
    
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        GM.objects.create(user=instance)
    instance.profile.save()
