from django.contrib import admin
# home kai models mai se contact ko as a model imprt kar liya
from home.models import Contact

# Register your models here.
admin.site.register(Contact)
# ab  aise karne se aapne contact model ko register kar liya
