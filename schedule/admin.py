from django.contrib import admin
from .models  import Availability, RecurringPattern, UnavailableDate

class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ['id','artist','day_of_week','start_time','end_time']


class RecurringPatternAdmin(admin.ModelAdmin):
    list_display = ['id','artist','days_of_week','start_time','end_time']

admin.site.register(Availability, AvailabilityAdmin)
admin.site.register(RecurringPattern, RecurringPatternAdmin)
admin.site.register(UnavailableDate)
