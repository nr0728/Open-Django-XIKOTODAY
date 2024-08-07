from django import forms
from .models import Topic, Entry
from users.models import Profile

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    anonymous = forms.BooleanField(label='以匿名形式发布', required=False)  # 添加复选框字段
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['school', 'age', 'motto', 'full_name', 'interests', 'location', 'b_Year', 'b_Month', 'b_Day', 'favorite_anime_character', 'favorite_anime', 'favorite_song', 'dream_destination', 'favorite_movie', 'favorite_book', 'dream']

  