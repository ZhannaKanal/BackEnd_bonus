from django.contrib import admin

# Register your models here.

from .models import Footer
admin.site.register(Footer)

from .models import Price1
admin.site.register(Price1)

from .models import Price2
admin.site.register(Price2)

from .models import Price3
admin.site.register(Price3)

from .models import Shop
admin.site.register(Shop)

from .models import Reg
admin.site.register(Reg)