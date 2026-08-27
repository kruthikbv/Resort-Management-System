from django.contrib import admin

# Register your models here. after the creating and signing in admin
from .models import Feature
admin.site.register(Feature)

#MODELS FOR SUITE BOOKING KBV
from .models import addsuite
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','phone', 'checkindate', 'checkintime','checkoutdate', 'checkouttime','roomtype',)
    search_fields = ('name', 'email')

admin.site.register(addsuite, AppointmentAdmin)



#MODELS FOR RESERVE TABLE KBV
from .models import addtable
admin.site.register(addtable)



#MODELS FOR VENUE TABLE KBV
from .models import addvenue
admin.site.register(addvenue)

from .models import Contact
admin.site.register(Contact)
