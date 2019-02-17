from django.db import models

class Contact(models.Model):
    sno = models.IntegerField()
    country = models.TextField(null=True, blank = True)
    description = models.TextField(null=True, blank = True)
    designaion = models.TextField(null=True, blank = True)
    points = models.DecimalField(max_digits=10, decimal_places=2, blank = True)
    price = models.DecimalField(max_digits=10, decimal_places=2,  blank = True)
    province = models.TextField(null = True,blank=True)
    region_1 = models.TextField(null=True,blank=True)
    region_2 = models.TextField(null=True,blank=True)
    variety = models.TextField(null = True,blank=True)
    winery = models.TextField(null = True,blank=True)

    def __str__(self):
        return f'{self.sno} {self.country} {self.variety} {self.winery}'
# Create your models here.
