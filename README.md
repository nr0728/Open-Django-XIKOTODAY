# XIKOTODAY OPEN

### 版权声明与免责声明

本软件由[胡哲涵]（以下简称“版权所有者”）根据GNU General Public License v3（以下简称“GPLv3”或“本许可证”）发布。版权所有者对本软件享有完整版权，并保留所有相关权利。

根据GPLv3的规定，用户享有以下权利：

1. **自由使用**：用户可以自由地修改、复制、分发本软件，以及以其他方式使用本软件，但须遵循GPLv3的条款与条件。
2. **衍生作品**：对于基于本软件创建的任何衍生作品（包括但不限于软件或服务），如包含对本软件的修改，必须按照GPLv3的条款进行分发，除非获得版权所有者的书面许可。

**特别强调**：

**版权标识与更新服务**：用户在使用本软件过程中，严禁擅自删除或篡改软件中的版权标识信息。任何未经版权所有者明确书面同意而删除或篡改版权标识的行为，将被视为严重侵犯本软件的版权。对于此类侵权行为，版权所有者将立即停止向侵权者提供任何后续的安全更新、功能升级或其他技术支持服务。侵权者将自行承担因无法获取官方更新而导致的一切风险与后果，并且版权所有者保留依法追究其侵权责任的权利。

**责任限制**：
版权所有者对因使用本软件而产生的直接、间接、特殊、附带或结果性损害不承担责任，包括但不限于用户在使用本软件搭建的论坛上发布的任何内容，尤其是违法言论。违法言论的法律责任应由实际发布者或论坛运营者承担。此外，版权所有者对因用户使用本软件产生的内容合法性问题导致的任何法律责任亦不承担责任。

**部署与公开使用限制**：
用户在基于本软件项目创建的任何网站、服务或应用（以下简称“部署项目”）进行公网部署或对不特定公众开放使用时，必须事先在本项目讨论区取得版权所有者的书面许可。未经许可的公网部署或公开使用行为，将被视为对本软件版权的严重侵犯。对于此类侵权行为，版权所有者有权要求立即停止部署项目的服务，并保留采取法律手段追究侵权者责任的权利，包括但不限于要求赔偿经济损失、公开道歉及消除影响。

**用户义务**：
用户在下载、安装和使用本软件时，务必仔细阅读并严格遵守本版权声明与免责声明，以及其他相关法律法规。任何违反本声明的行为，都将可能导致法律责任。用户在使用本软件过程中，应确保自身行为符合法律法规要求，不得利用本软件从事任何违法、违规或侵犯他人合法权益的活动。

**免责声明的完整性与更新**：
本版权声明与免责声明构成用户与版权所有者之间关于本软件使用的完整协议。版权所有者保留随时更新、修改或补充本声明的权利，任何更新、修改或补充将在本项目讨论区发布后立即生效。用户有义务定期查阅本声明的最新版本，以确保自身行为始终符合声明要求。如用户继续使用本软件，视为接受并同意声明的更新、修改或补充内容。

**法律适用与争议解决**：
本声明的解释、效力及双方因使用本软件产生的争议，均适用中华人民共和国法律。如双方就本声明或使用本软件产生的任何争议无法协商解决，任何一方均有权将争议提交至版权所有者所在地有管辖权的人民法院诉讼解决。

通过以上补充与完善，本声明旨在更全面地保护版权所有者的合法权益，明确用户在使用本软件过程中的权利与义务，以及在未经许可的公网部署或公开使用、违反声明规定等情况下可能面临的法律责任，同时强化了声明的完整性与更新机制，以及法律适用与争议解决条款，以适应法律环境变化及保护各方权益的需求。


## 项目简介

XIKOTODAY由XIKOGroup的胡哲涵开发，因本人无力维护且发现其的技术含量已经让我沉浸于舒适圈了，故基于GPL v3协议开源。  

## 关键信息

本项目的部署基于Django框架，快捷方便。我将不定期发布安全及功能更新。欢迎提交你的功能及安全更新。我要必要提醒你，你如果希望将此项目部署并用作生产环境，learning_log/settings.py文件中有重要的安全配置信息，请在部署你的项目时更换SECRET_KEY的内容，其次DEBUG请设置为False，并按照你的服务器配置ALLOWED_HOSTS，防止HTTP Host头攻击！  
当然，如果你只是想在本地玩一玩，或者仅仅为你的班级、朋友设立交流论坛，就不用那么繁琐的配置安全项信息了。

## 作者介绍

胡哲涵，现就读于重庆市沙坪坝小学6年级13班。
(更新，毕业了。我想那个女孩。)  
擅长C++基础语法及算法，Python项目开发，懂一点点前端。 
最喜欢《名侦探柯南》里的灰原哀，真的可爱得令人忘记了尘世。本人头像便是哀！  
唯一喜欢的CP是柯哀，默契，关键是有夫妻相！ 

### 前述

  此项目由本人参考《Python编程：从入门到实践》的Django章节的部分代码开发而来，但对于新版Django进行了适配，并且增加了许多新功能。

### 在你的计算机上面部署本项目

```
git clone http://github.com/lovehuiyuanai/Open-Django-XIKOTODAY.git
```

使用Git拉取本项目

##### 1.1 终端切换到此目录，创建虚拟环境

```
pip install Django
```

##### 1.5 创建Django 数据库

```
python manage.py migrate
```

##### 1.6 迁移数据库

```
python manage.py makemigrations
```

##### 1.7 创建超级管理员（站长）

```
python manage.py createsuperuser
```

##### 1.8 XIKOTODAY启动！

```
python manage.py runserver
```

## 项目进展

* Apr 19, 2024 发布XIKOTODAY OPEN V0.0.1，RED测试版，因众多安全问题不建议下载部署，6月会更新V0.0.2 OPEN版本，会改进众多安全隐患，增加更多功能，敬请期待。

* Aug 7, 2024 发布XIKOTODAY OPEN V0.1.5，ORANGE正式发行版。仍存在被入侵的安全隐患，但可以作为一个私人论坛了。
