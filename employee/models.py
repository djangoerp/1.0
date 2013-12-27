from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from company.models import *

class Employee(models.Model):

	# Fields 
	user = models.OneToOneField(User)
	name = models.CharField('Name', max_length=50)
	description = models.TextField('Description')
	id_card = models.CharField('ID Card', max_length=50)
	company = models.ForeignKey(Company)
	role = models.ForeignKey('EmployeeRole')

	class Meta:
		verbose_name = _('Employee')
		verbose_name_plural = _('Employees')

	def __unicode__(self):
		pass

class EmployeeRole(models.Model):

	#Fields
	name = models.CharField('Name', max_length=50)

	class Meta:
		verbose_name = _('Employee Role')
		verbose_name_plural = _('Employee Roles')

	def __unicode__(self):
		pass
    