from django.contrib import admin
from visitorsapp.models import Visitor

class VisitorAdmin(admin.ModelAdmin):
	list_display=['name','address','mobile_number']

admin.site.register(Visitor,VisitorAdmin)	