from django.contrib import admin
from .models import *#accessing our classes which are our tables upon which we are going to build interfaces so that administrators can fill in the period of stay at school from the admin panel/dashboard
#from .models import Catergorystay, Babe


# Register your models here.
admin.site.register(CategoryStay)
admin.site.register(Babe)
admin.site.register(Payment)



