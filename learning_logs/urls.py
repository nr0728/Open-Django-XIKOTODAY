from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
	# 主页
	path('',views.index, name='index'),

	# 显示所有主题
	path('topics/', views.topics, name='topics'),

	# 特定主题的详细页面
	path("topics/<int:topic_id>/", views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/?P<topic_id>\d+)/', views.new_entry, name='new_entry'),
    path('docs/1', views.pri, name='Privacy'),
    path('docs/2', views.mzsm, name='mzsm'),
    path('profile/<int:user_id>/', views.profile, name='user_profile'),
	path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('OK', views.OK, name='OK')
]

