from django.contrib import admin
from django import forms
from .models import Profile

class ProfileAdminForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'b_Year': forms.NumberInput(),  # 修改为使用数字输入框
        }

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    form = ProfileAdminForm
    list_display = ('user', 'age', 'motto', 'location', 'school', 'show_birthday')  # 在admin界面中显示的字段
    list_filter = ('location',)  # 添加一个筛选器
    search_fields = ('user__username', 'full_name', 'location')  # 添加一个搜索框

    def show_birthday(self, obj):
        if obj.b_Year and obj.b_Month and obj.b_Day:
            return f"{obj.b_Year}-{obj.b_Month}-{obj.b_Day}"  # 根据b_Year, b_Month, b_Day字段组合生日字符串
        else:
            return ""  # 如果生日字段缺少信息，则返回空字符串

    show_birthday.short_description = 'Birthday'  # 设置在Admin界面中的生日字段标题




