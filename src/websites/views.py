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
		for entry in entries_to_delete
			entry.delete()
		
		# get the new entries and save them to the database	
		data = feedparser.parse(x_website.feed)
		for i in range(0, 20):         
			xEntry = data.entries[i]
			xTitle = xEntry.title
			xLink = xEntry.link  
			entry = Entry(website=x_website, title=xTitle, url=xLink)
			entry.save()
			
	return render_to_response('websites/index.html', {'websites': websites})
# index = cache_page(index, 60 * 60)
