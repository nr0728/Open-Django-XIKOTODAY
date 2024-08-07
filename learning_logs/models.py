from django.db import models
from django import forms
from django.contrib.auth.models import User  # 导入Django的用户模型
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Topic(models.Model):
    text = models.CharField(max_length=200, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text

class TownTalk(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

 
class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    publisher_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries')
    anonymous = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False) 
    tags = models.CharField(max_length=100)  # 添加一个字段来记录标签
    towntalk = models.CharField(max_length=100) 
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return self.text[:50] + '...'


@receiver(pre_save, sender=Entry)
def update_entry_verification(sender, instance, **kwargs):
    if instance.publisher_user.profile.is_verified:
        instance.is_verified = True
    else:
        instance.is_verified = False

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}



# 在文件的末尾导入Topic模型
from .models import Topic
