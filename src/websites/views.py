from django.shortcuts import render_to_response
from src.websites.models import Website   
from src.websites.models import Entry   
from django.views.decorators.cache import cache_page
import feedparser

def index(request):
	websites = Website.objects.all()  
	
	for x_website in websites:
		# remove the old entries from the database
		entries_to_delete = Entry.objects.filter(website=x_website)  
		if entries_to_delete:
			for entry_to_delete in entries_to_delete:
				entry_to_delete.delete()   
		
		# get the new entries and save them to the database	    
		# save a maximum of 20 entries into the database
		data = feedparser.parse(x_website.feed)      
		number_of_entries = len(data['entries']) 
		entries_to_save = 20
		if number_of_entries < 20:      
			entries_to_save = number_of_entries
		for i in range(0, entries_to_save):         
			xEntry = data.entries[i]
			xTitle = xEntry.title
			xLink = xEntry.link  
			entry_to_save = Entry(website=x_website, title=xTitle, url=xLink)
			entry_to_save.save()
			
	return render_to_response('websites/index.html', {'websites': websites})
index = cache_page(index, 60 * 60)
