
**<h1>santabanta</h1>**    
This is a Scrapy project to scrape wallpapers from website www.santabanta.com.  

**<h3>Items</h3>**    

The items scraped by this project are High Definition Images, and the item is defined in the class:  

SantaBanta.items.SantaBantaItem  
See the source code for more details.      

**<h3>Spiders</h3>**    
There are 2 spiders in this project for  wallpapers(santbanta) and image gallery (santabanta2)

**<h5>wallpapers</h5>**
This spider scraps High Definition wallpapers  
Scrap url: http://www.santabanta.com/wallpapers   

Examples:   
global-celebrities(f)      
scrapy crawl santabanta -a wallpapers=eva-green   

local-celebrities(m)   
scrapy crawl santabanta -a wallpapers=hrithik-roshan   
   
cars     
scrapy crawl santabanta -a wallpapers=mercedez-benz  

bikes   
scrapy crawl santabanta -a wallpapers=honda-bikes  
scrapy crawl santabanta -a wallpapers=aprilia   


The naming convention for running sipder keyword arguments is small case first name and last name seperated by - (hrithik-roshan)    

The santabanta spider scrapes wallpapers with paging and finds those beautiful Images.     

This spider doesn't crawl the entire santabanta site but only a few pages by default (defined in the wallpapers section).   These pages are:    

 

So, if you run the spider,it will scrape only those pages only for wallpapers which are customized to save in settings.py (IMAGES_STORE).Cutomization for resolution of wallpapers can be done adjusting height and weidth in setting.py   

**<h5>images</h5>**
This spider scraps various bollywood events gallery pics like parties,music or film launch etc.  
Scrape url example:http://www.santabanta.com/images/sonam-kapoor      
scrapy crawl santabanta -a images=sonam-kapoor    


**<h3>Image Pipelines</h3>**      

This project uses a cutomized Image pipeline to rename images :    

santabanta.pipelines.MyImagesPipeline    

Please change IMAGE_STORE in settings.py to directory location you need to scrape images into.
