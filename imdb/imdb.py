from bs4 import BeautifulSoup
import urllib2
import Image
import cStringIO

film_id = '0423409'
url = 'http://www.imdb.com/title/tt%s/' % (film_id)
soup = BeautifulSoup(urllib2.urlopen(url).read())
link = soup.find(itemprop="image")


imgdata = urllib2.urlopen(link["src"].read()
img = Image.open(cStringIO.StringIO(imgdata))
img.save("goog.jpg")


def stealStuff(file_name,file_mode,base_url):
	from urllib2 import Request, urlopen, URLError, HTTPError
	
	#create the url and the request
	url = base_url + file_name
	req = Request(url)
	
	# Open the url
	try:
		f = urlopen(req)
		print "downloading " + url
		
		# Open our local file for writing
		local_file = open(file_name, "w" + file_mode)
		#Write to our local file
		local_file.write(f.read())
		local_file.close()
		
	#handle errors
	except HTTPError, e:
		print "HTTP Error:",e.code , url
	except URLError, e:
		print "URL Error:",e.reason , url


# Set the range of images to 1-50.It says 51 because the 
# range function never gets to the endpoint.
image_range = range(1,51)

# Iterate over image range
for index in image_range:
	
	base_url = 'http://www.techniqal.com/'
	#create file name based on known pattern 
	file_name =  str(index) + ".jpg"
	# Now download the image. If these were text files, 
	# or other ascii types, just pass an empty string 
	# for the second param ala stealStuff(file_name,'',base_url)
	stealStuff(file_name,"b",base_url)


