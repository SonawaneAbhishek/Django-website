from django.contrib import admin

from user.views import contactus
from . models import Contactus
# develop-6402
# Register your models here

admin.site.register(Contactus)