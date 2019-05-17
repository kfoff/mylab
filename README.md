## ПОРЯДОК ОФОРМЛЕНИЕ КОДА

#### ОБЩАЯ СТРУКТУРА ПРОЕКТА

> Представление общей структуры проекта

```bash
myproject
├── dj
│   ├── __init__.py
│   ├── settings.py          # основные настройки
│   ├── settings_local.py    # личные настройки проекта
│   ├── urls.py
│   ├── views.py
│   ├── utils.py
│   └── wsgi.py
├── node
│   ├── migrations
│   │   └── ...
│   ├── templates
│   │   ├── templatetags
│   │   ├── __init__.py
│   │   └── nodetag.py
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── fooapp
│   ├── migrations
│   │   └── ...
│   ├── templates
│   │   ├── foo_list.html
│   │   ├── foo_add.html
│   │   ├── foo_edit.html
│   │   └── foo_del.html
│   ├── templatetags
│   │   ├── __init__.py
│   │   └── footag.py
│   ├── __init__.py
│   ├── admin.py
│   ├── models.py
│   ├── form.py
│   ├── api.py
│   ├── urls.py
│   └── views.py
├── static
│   ├── ...
├── media
│   ├── ...
├── template
│   ├── _form.html
│   ├── 404.html
│   ├── base.html
│   ├── paginator.html
│   └── xpaginator.html
└──manage.py
```

#### НАСТРОЙКИ ПРОЕКТА dj.settings и dj.settings_local

> основные настройки храним в ```settings.py```, личные настройки проекта храним в ```settings_local.py``` который не будет выгружаться в репозиторий

пример использования settings.py:
```python
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'

DEBUG = True

ALLOWED_HOSTS = ['*']

SITE_ID = 1

# Application definition
INSTALLED_APPS = [
	'node',
	'fooapp',
	...
]

WSGI_APPLICATION = 'dj.wsgi.application'

DATE_INPUT_FORMATS = ['%d-%m-%y','%d-%m-%Y']

DATETIME_INPUT_FORMATS = ['%d-%m-%y %H:%M:%S','%d-%m-%Y %H:%M:%S']

LOGIN_URL = '/user/login'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

try:
	from dj.settings_local import STATICFILES_DIRS
except:
	STATIC_ROOT = os.path.join(BASE_DIR, 'static')

#STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'), )
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# в конце файла settings.py подключаем кастомные настройки settings_local.py
try:
	from dj.settings_local import *
except:
	pass
```

кастомные настройки: settings_local.py

```python
# ваше текущее подключение к базе данных
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'mybase',
		'USER': 'myuser',
		'PASSWORD': 'mypass',
		'HOST': '192.168.0.XX',
		'PORT': '5432',
	}
}
```



#### ПРИЛОЖЕНИЕ app

> шаблон имени: **xxxxapp**

```python
# пример
INSTALLED_APPS = [
	'fooapp',
	'productapp',
	'newsapp',
	...
]
urlpatterns = [
	url(r'^', include('fooapp.urls')),
	url(r'^', include('productapp.urls')),
	url(r'^', include('newsapp.urls')),
	...
]
```

***

#### МОДЕЛЬ models.py

> названия моделей начинается с символа верхнего регистра, соблюдаем рекомендации Django

пример названия модели: **Foo**, **News**, **Product**

```python
# пример
class Foo(models.Model):
	id = models.AutoField(primary_key=True, unique=True) #обязательное поле
	
	#
	name = models.CharField(verbose_name='Название', max_length=255)
	title = models.CharField(verbose_name='title', max_length=255, blank=True)
	
	#
	pict = models.ImageField(upload_to=make_upload_file, verbose_name='Изображение')
	pict40 = ImageSpecField(source='pict', processors=[ResizeToFit(40, 40)], format='PNG', options={'quality': 95})
	pict100 = ImageSpecField(source='pict', processors=[ResizeToFit(100, 100)], format='PNG', options={'quality': 95})
	
	#
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) #user определяет принадлежность объекта к пользователю, доп. атрибуты null=True, blank=True
	
	#
	ctime = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
	# ctime выполняет функцию отслеживания даты создания объекта
	utime = models.DateTimeField(verbose_name='Дата обновления объекта', auto_now=True)
	# utime выполняет функцию отслеживания даты последнего обновления объекта
	# так же может быть обновлена принудительно, пример object.utime = datetime.datetime.now()
	
	#
	cuser = models.ForeignKey(User, related_name='foo_cuser', on_delete=models.CASCADE, blank=True, null=True,)
	muser = models.ForeignKey(User, related_name='foo_muser', on_delete=models.CASCADE, blank=True, null=True,)
	
	
	# seo оптимизация (для публичной части интернет страниц)
	seo_title = models.CharField(max_length=255, blank=True)
	seo_description = models.CharField(max_length=255, blank=True)
	seo_keywords = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return u'%s %s' % (self.id, self.name)
		
	class Meta:
		ordering=['-id']
		verbose_name = 'Foo'
		verbose_name_plural = 'Foo'
		
```

все связи моделей по возможности делаем через ```models.ForeignKey()```
```python
# пимер связи таблицы Foo и User по полю user
# плюсы подхода, автоматические удаление связанных полей
class Foo(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	
```

```python
# использование связи ManyToMany рекомендуется использовать в крайних случаях
# минусы подхода, ручное удаление связанных полей
class Foo(models.Model):
	user = models.ManyToManyField(User)
	
```

***

#### УПРАВЛЕНИЕ ЭЛЕМЕНТАМИ admin.py

```python
# пример
from .models import *

class FooAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'cdate', 'status', 'user', 'message', )
	
	list_filter = ['user', 'status',]
	search_fields = ['id', 'name', 'message',]
	
	save_on_top = True

	def short_ctime(self, obj):
		return obj.ctime.strftime("%d-%m-%Y %H:%M")
	short_ctime.short_description  = 'ctime'
	short_ctime.allow_tags = True
	
admin.site.register(Foo, FooAdmin)
```

***

#### УПРАВЛЕНИЕ ЭЛЕМЕНТАМИ panel.py

шаблон имени класса

- список элементов: ```panel_названиемодели_list(ListView)```
- добавление элемента: ```panel_названиемодели_add(CreateView)```
- удаление элемента: ```panel_названиемодели_del(DeleteView)```
- редактирование элемента: ```panel_названиемодел_edit(UpdateView)```


```python
# пример
from acl.views import get_object_or_denied
# (('A', 'All'), ('L', 'Список'), ('R', 'Чтение'), ('C', 'Создание'), ('U', 'Редактирование'),)

class panel_newslist_list(ListView):
	model = newslist
	template_name = 'panel_newslist_list.html'
	# для вывода списка элементов в шаблоне использовать переменную object_list

	def dispatch(self, request, *args, **kwargs):
		get_object_or_denied(self.request.user, 'newslist', 'L') # проверяем права
		return super(panel_newslist_list, self).dispatch(request, *args, **kwargs)
		
		
class panel_newslist_add(CreateView):
	model = newslist
	template_name = 'panel_newslist_add.html'
	fields = ['name', 'pict']

	def dispatch(self, request, *args, **kwargs):
		get_object_or_denied(self.request.user, 'newslist', 'C') # проверяем права
		return super(panel_newslist_add, self).dispatch(request, *args, **kwargs)

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		instance.save()
		self.data = instance
		return super(panel_newslist_add, self).form_valid(form)

	def get_success_url(self):
		return reverse_lazy('panel_newslist_list')
		

class panel_newslist_del(DeleteView):
	model = newslist
	template_name = 'panel_newslist_del.html'

	def dispatch(self, request, *args, **kwargs):
		get_object_or_denied(self.request.user, 'baner', 'U') # проверяем права
		return super(panel_newslist_del, self).dispatch(request, *args, **kwargs)

	def get_success_url(self):
		return reverse_lazy('panel_newslist_list')
		
		
class panel_newslist_edit(UpdateView):
	model = newslist
	template_name = 'panel_newslist_edit.html'
	fields = ['url', 'pict']

	def dispatch(self, request, *args, **kwargs):
		get_object_or_denied(self.request.user, 'baner', 'U') # проверяем права
		return super(panel_newslist_edit, self).dispatch(request, *args, **kwargs)

	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.user = self.request.user
		instance.save()
		self.data = instance
		return super(panel_newslist_edit, self).form_valid(form)

	def get_success_url(self):
		return reverse_lazy('panel_newslist_list')
		
```

***

#### РОУТИНГ urls.py

- url типа **'/panel/newslist/list/'** передает управление классу **panel_newslist_list** (```/``` замена на ```_```)

- каноническое имя url идентично названию класса **panel_newslist_list**

- при обращении к url через ```reverse_lazy('panel_newslist_list')``` понимаем, что будет вызван ```class panel_newslist_list(ListView):``` из **panel.py** приложения

- завершающий символ ```?``` обязателен для url ```'^/newslist/list/?$'```, так как позволяет пользователям открывать страницу по адресам **/newslist/list/** и **/newslist/list**

```python
# пример
from django.contrib.auth.decorators import login_required

from .views import *
from .panel import *

urlpatterns = [
	# views.py публичная часть
	re_path('^/newslist/list/?$', newslist_list.as_view(), name='newslist_list'),
	# panel.py приватная часть
	re_path('^/panel/newslist/list/?$', login_required(panel_newslist_list.as_view()), name='panel_newslist_list'),
	re_path('^/panel/newslist/add/?$', login_required(panel_newslist_add.as_view()), name='panel_newslist_add'),
	re_path('^/panel/newslist/del/(?P<pk>\d+)/?$', login_required(panel_newslist_del.as_view()), name='panel_newslist_del'),
	re_path('^/panel/newslist/edit/(?P<pk>\d+)/?$', login_required(panel_newslist_edit.as_view()), name='panel_newslist_edit'),
]
```

***

#### ШАБЛОНЫ templates

шаблоны приложений храняться в каталоге **newsapp/templates**

публичная часть
- шаблон наследования: **template/base.html**
- список элементов: **newsapp/templates/newslist_list.html**

приватная часть
- шаблон наследования: **template/panel_base.html**
- список элементов: **newsapp/templates/panel_newslist_list.html**
- добавление элемента: **newsapp/templates/panel_newslist_add.html**
- удаление элемента: **newsapp/templates/panel_newslist_del.html**
- редактирование элемента: **newsapp/templates/panel_newslist_edit.html**

```html
<!-- пример базового шаблона приватной части -->
{% extends "panel_base.html" %}
{% block title %}Панель управления{% endblock %}
{% block description %}Панель управления{% endblock %}
{% block keywords %}{% endblock %}

{% block content %}

{% load nodetag %}

{% load newsapptag %} <!-- если необходимо подключаем кастомные теги -->

{% include "paginator.html" %} <!-- если необходимо подключаем пагинатор -->

{% endblock %}

```

```html
<!-- пример базового шаблона публичной части элемента детально -->
{% extends "base.html" %}
{% block title %} {{ object.seo_title }} {% endblock %}
{% block description %} {{ object.seo_description }} {% endblock %}
{% block keywords %} {{ object.seo_keywords }} {% endblock %}

{% block content %}

{% load nodetag %}

{% load newsapptag %} <!-- если необходимо подключаем кастомные теги -->

<h1>{{ object.name }}</h1>

{% endblock %}
```

```html
<!-- пример базового шаблона публичной части списка элементов -->
{% extends "base.html" %}
{% block title %}{% endblock %}
{% block description %}{% endblock %}
{% block keywords %}{% endblock %}

{% block content %}

{% load nodetag %}

{% load newsapptag %} <!-- если необходимо подключаем кастомные теги -->

{% for i in object_list %} <!-- забираем данные из встроенной переменной object_list -->
	{{ i.name }}
{% endfor %}

{% include "paginator.html" %} <!-- если необходимо подключаем пагинатор -->

{% endblock %}
```

комментирование участков кода в шаблоне средствами шаблонизатора Django 
```
{% comment %}
<div class="test">test</div>
{% endcomment %}
```
	
плохой пример комментирования, отнимает ресурсы
```
<!-- 
<div class="test">test</div>
-->
```





***

#### КАСТОМЫНЕ ТЭГИ templatetags
кастомыне теги храняться в  **newsapp/templatetags/newsapptag.py**


***
### РЕЦЕПТЫ

счетчик просмотров ```pip install django-hitcount```
```python
# in models.py
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCountMixin
from hitcount.models import HitCount

class newss(models.Model, HitCountMixin):
	hitcount = GenericRelation(HitCount, object_id_field='id', related_query_name='hit_count_generic_relation',)

# in views.py
from hitcount.views import HitCountDetailView

class newss_detail(HitCountDetailView): # класс HitCountDetailView наследует класс DetailView
	model = newss
	template_name = 'newss_detail.html'
	count_hit = True

# in template
{% for newsitem in object_list %}
	newsitem.hit_count.hits
{% endfor %}
```
Телеграм рассылка
Для исспользование телеграм рассылки импортируем 2 ф-ии
```python
from notifyapp.views import get_message, send_message_in_chat
```
```python
value_chat = get_message('biditem_add', self.request.user, path)
```
'biditem_add' - шаблон оповещения. 
Шаблон хранится в notifyapp.models, соответственно что бы оповещение работало предварителбно в таблице
notifytemplate создать запись
self.request.user - пользователь который подставится в шаблон
path - ссылка передающаяся в шаблон оповещения.
```python
send_message_in_chat(value_chat)
```


