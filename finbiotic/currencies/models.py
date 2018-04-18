from django.utils.encoding import python_2_unicode_compatible
import datetime
from django.db import models
from django.utils import timezone


# @python_2_unicode_compatible # only if you need to support Python 2
class Order(models.Model):
    order_text = models.CharField(verbose_name='Instrument', max_length=10)
    time = models.DateTimeField('Time')
    units = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=6, decimal_places=5)

    def created(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.time <= now

    created.admin_order_field = 'time'
    created.boolean = True
    created.short_description = 'Order Created?'


@python_2_unicode_compatible # only if you need to support Python 2
class Fill(models.Model):
    instrument = models.ForeignKey(Order, on_delete=models.CASCADE)
    time = models.DateTimeField('Time')
    fill_text = models.CharField(verbose_name='Stop Loss, Take Profit', max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=5)

    def __str__(self):
        return self.fill_text
