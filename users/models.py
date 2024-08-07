from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True, null=True)
    motto = models.CharField(max_length=100, blank=True)
    full_name = models.CharField(max_length=100, blank=True)
    interests = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    b_Year = models.IntegerField(blank=True, null=True)
    b_Month = models.IntegerField(blank=True, null=True)
    b_Day = models.IntegerField(blank=True, null=True)
    favorite_anime_character = models.CharField(max_length=100, blank=True)
    favorite_anime = models.CharField(max_length=100, blank=True)
    favorite_song = models.CharField(max_length=100, blank=True)
    dream_destination = models.CharField(max_length=100, blank=True)
    favorite_movie = models.CharField(max_length=100, blank=True)
    favorite_book = models.CharField(max_length=100, blank=True)
    dream = models.TextField(max_length=100,blank=True)
    is_verified = models.BooleanField(default=False)  # 认证状态
    remark = models.TextField(max_length=100,blank=True)  # 备注
    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Entry(models.Model):
    # 其他字段定义
    publisher_user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)

def update_entry_verification(sender, instance, **kwargs):
    if hasattr(instance.publisher_user, 'profile'):
        if instance.publisher_user.profile.is_verified:
            instance.is_verified = True
        else:
            instance.is_verified = False
    else:
        instance.is_verified = False

post_save.connect(update_entry_verification, sender=Entry)
