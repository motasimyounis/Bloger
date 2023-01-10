from django.contrib import admin
from .models import *
# Register your models here.

class NewAdmin(admin.ModelAdmin):
    list_display = ('id','title','date_post','main','main2','most_popular', 'trending' ,'type' ,'cate' )
    list_editable = ('title', 'most_popular', 'trending' ,'type','main','main2' )
    search_fields = ['title']
    
admin.site.register(New,NewAdmin)
admin.site.site_header = 'مجلة الغد'
admin.site.site_title = 'مجلة الغد'
