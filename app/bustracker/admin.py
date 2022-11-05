from django.contrib import admin
from .models import Bus, Route, Stop,  Driver

# Register your models here.
admin.site.register(Bus)
admin.site.register(Route)
admin.site.register(Stop)
#admin.site.register(RouteStop)
admin.site.register(Driver)

