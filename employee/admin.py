from django.contrib import admin
from django.conf import settings
from models import *

class EmployeeAdmin(admin.ModelAdmin):
	 fields = ['user','name','company','id_card','role','description']
	 list_display = ['name','user']

admin.site.register(Employee,EmployeeAdmin)

