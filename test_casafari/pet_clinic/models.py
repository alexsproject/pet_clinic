from django.db import models

# Create your models here.
class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    pet_type = models.CharField(max_length=200, verbose_name='Type')
    pet_name = models.CharField(max_length=200, verbose_name='Name')
    pet_birthday = models.DateField(max_length=200, verbose_name='Birthday')
    pet_age = models.IntegerField()
    pet_height = models.IntegerField()
    pet_weight = models.FloatField()
    pet_
    order_phone = models.CharField(max_length=200, verbose_name='Phone')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
