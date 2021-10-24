from django.contrib import admin
from .models import Newcat,Newslearnbbc,Newslearneuronews,Newslearnwion

#admin.site.register(Newcat)

@admin.register(Newcat)
class Newcatadmin(admin.ModelAdmin):
    list_display=('sentence','label')
admin.site.register(Newslearnwion)
admin.site.register(Newslearnbbc)
admin.site.register(Newslearneuronews)
