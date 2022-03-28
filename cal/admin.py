
from django.contrib import admin
from . models import Cal
class CalAdmin(admin.ModelAdmin):
	list_display = ('sr', 'img_url', 'uni', 'state', 'title', 'date', 'link')

admin.site.register(Cal, CalAdmin)