from src.websites.models import Website
from src.websites.models import Entry
from django.contrib import admin  

class EntryInline(admin.TabularInline):
	model = Entry
	  
class WebsiteAdmin(admin.ModelAdmin):
	fields = ['title', 'url', 'feed'] 
	inlines = [EntryInline]

admin.site.register(Website, WebsiteAdmin)