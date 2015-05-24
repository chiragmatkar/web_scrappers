
**<h1>santabanta</h1>**    
This is a Scrapy project to scrape wallpapers from website www.santabanta.com.  

**<h3>Items</h3>**    

The items scraped by this project are High Definition Images, and the item is defined in the class:  

SantaBanta.items.SantaBantaItem  
See the source code for more details.      

**<h3>Spiders</h3>**    

This project contains santabanta spider in spiders/santa_spider.py that you can see by running:   

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

default without arguments   
scrapy crawl santabanta (default wallpapers=kelly-brook)


The naming convention for running sipder keyword arguments is small case first name and last name seperated by - (hrithik-roshan)    

The santabanta spider scrapes wallpapers with paging and finds those beautiful Images.     

This spider doesn't crawl the entire santabanta site but only a few pages by default (defined in the wallpapers section).   These pages are:    

http://www.santabanta.com/wallpapers    

So, if you run the spider,it will scrape only those pages only for wallpapers which are customized to save in settings.py (IMAGES_STORE).Cutomization for resolution of wallpapers can be done adjusting height and weidth in setting.py   

**<h3>Image Pipelines</h3>**      

This project uses a cutomized Image pipeline to rename images :    

santabanta.pipelines.MyImagesPipeline    
