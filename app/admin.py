from django.contrib import admin

# Register your models here.


from app.models import *


admin.site.register(profile)
# here no need to register the User Because User is the Builtin module thats why no need to register the module
# thats why only User defined data should be registerd so we are directly registered the perticular Profile only