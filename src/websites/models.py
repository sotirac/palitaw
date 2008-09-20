from django.db import models

class Category(models.Model):
	title = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.title
		   	
class Website(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=200)
	url = models.CharField(max_length=200) 
	feed = models.CharField(max_length=200)  
	
	def __unicode__(self):
		return self.title
		
	def entries_one(self):
		return Entry.objects.filter(website=self)[0:1] 
		  
	def entries_one_to_ten(self):
		return Entry.objects.filter(website=self)[0:10] 
		
	def entries_eleven_to_twenty(self):
		return Entry.objects.filter(website=self)[11:20] 
		
	  
class Entry(models.Model): 
	website = models.ForeignKey(Website)
	title = models.CharField(max_length=200)
	summary = models.TextField()   
	url = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.title