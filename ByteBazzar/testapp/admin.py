from django.contrib import admin
from testapp.models import User

# Register your models here.
class customerInfoAdmin(admin.ModelAdmin):
    list_display=['username','first_name','last_name','email','password']
admin.site.register(User,customerInfoAdmin)
