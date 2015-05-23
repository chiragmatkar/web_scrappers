#Web scraper to download Indian Actresses pics from santabanta
#GPL License developed by Chirag Matkar
#

import urllib
import os


def makedir(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)
	else:
	 return
			 
			
with open("indian_actresses.txt") as f:
    for actress in f:
		if '#' in actress: 
			continue
		else:
			actress=actress.replace("\n","")
			print actress
			type=actress.split(" ")
			fname=type[0]
			lname=type[1]
			lowerfname=fname.lower()
			lowerlname=lname.lower()
			actress.strip()
			makedir(actress)
			for i in xrange(1,200):
				link="http://media1.santabanta.com/full5/Indian%20%20Celebrities(F)/"+ str(fname)+"%20"+ str(lname) +"/"+str(lowerfname)+"-"+ str(lowerlname)+"-"+str(i)+"a.jpg"					
				status = urllib.urlopen(link).getcode()		
				if status == 200:
					print "Downloading ... ",link
					urllib.urlretrieve(link, actress+"/"+actress+"_"+str(i)+".jpg")	
				elif status == 404: #if status is equal to 404 (NOT FOUND) 
					print   link,". Does not exist!!'" #display error
				else: #Any other message then display error and the status code
					print 'Unknown Error:', status