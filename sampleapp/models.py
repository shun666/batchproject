# coding: utf-8

from django.db import models

# Create your models here.


class Item(models.Model):
    """
    """
    name = models.CharField('Name', max_length=100)
    date = models.DateField('Date', null=True, blank=True)
    status = models.IntegerField(
        'Status', null=True, blank=True)
    category = models.IntegerField('Category', null=True, blank=True)
    enabled = models.BooleanField('Enabled/Disabled', )
    value = models.DecimalField('Number', decimal_places=3, max_digits=10, null=True, blank=True)
    memo = models.TextField('Memo',  null=True, blank=True)

    def get_enabled_display(self):
        if self.enabled in [True, 1, '1']:
            return u"有効"
        elif self.enabled in [False, 0, '0']:
            return u"無効"

    get_enabled_display.short_description = 'Enabled/Disabled'

    def get_value_display(self):
        if self.value is not None:
            return "{:,}".format(self.value)

    get_value_display.short_description = 'Number'
    get_value_display.align = "right"

    name.truncate_length = 40

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'


class BatchWork(models.Model):
    """
    """
    name = models.CharField('Name', max_length=100)
    date = models.DateField('Date', null=True, blank=True)
