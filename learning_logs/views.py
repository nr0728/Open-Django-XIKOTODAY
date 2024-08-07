from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Topic
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from users.models import Profile
from .forms import ProfileForm

def index(request):
    '''学习笔记的主页'''
    return render(request, 'learning_logs/index.html')

def topics(request):
    '''显示所有的主题'''
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    '''显示特定主题的所有条目'''
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
	'''添加新主题'''
	if request.method != 'POST':
		# 未提交数据，创建一个新表单
		form = TopicForm()
	else:
		# POST提交的数据，对数据进行处理
		form = TopicForm(request.POST)		
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('learning_logs:topics'))

	context = {'form': form}
	return render(request, 'learning_logs/new_topic.html', context)

def mzsm(request):
    '''学习笔记的主页'''
    return render(request, 'learning_logs/mzsm.html')


@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if request.method == 'POST':
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.publisher_user = request.user  # 将当前登录用户关联到条目的发布者字段

            # Check if 'anonymous' field is present in the form data
            if 'anonymous' in form.cleaned_data:
                new_entry.anonymous = form.cleaned_data['anonymous']

            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    else:
        form = EntryForm()

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)




@login_required  # 这样只有登录用户才能添加新主题
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.publisher_user = request.user  # 将当前登录用户关联到主题的发布者字段
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def pri(request):
    '''学习笔记的主页'''
    return render(request, 'learning_logs/pri.html')


def OK(request):
    '''学习笔记的主页'''
    return render(request, 'learning_logs/OK.html')

def profile(request, user_id):
    user_profile = get_object_or_404(Profile, user_id=user_id)  # 使用profile小写形式来获取用户资料

    context = {'user_profile': user_profile}
    return render(request, 'learning_logs/profile.html', context)


from django.shortcuts import render, redirect
from .forms import ProfileForm
from users.models import Profile
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('/OK') 
          # 重定向到用户的个人主页
    else:
        if hasattr(request.user, 'profile'):  # 检查用户是否存在 profile 对象
            form = ProfileForm(instance=request.user.profile)
        else:
            profile = Profile(user=request.user)
            profile.save()
            form = ProfileForm(instance=profile)
    return render(request, 'learning_logs/edit_profile.html', {'form': form})


