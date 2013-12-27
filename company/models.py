from django.db import models
from django.utils.translation import ugettext as _

class Company(models.Model):

	#Fields
	name = models.CharField('Company Name', max_length=50)

	class Meta:
		verbose_name = _('Company')
		verbose_name_plural = _('Companies')

	def __unicode__(self):
		pass


# Create your models here.
