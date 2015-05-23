
**<h1>santabanta</h1>**    
This is a Scrapy project to scrape Wallpapers from website www.santabanta.com.  

**<h3>Items</h3>**    

The items scraped by this project are High Definition Images, and the item is defined in the class:  

SantaBanta.items.SantaBantaItem  
See the source code for more details.      

**<h3>Spiders</h3>**    

This project contains one spider called santa_spider.py that you can see by running:   

Examples:   
scrapy crawl santabanta -a wallpapers=eva-green   
scrapy crawl santabanta -a wallpapers=hrithik-roshan   
scrapy crawl santabanta (default wallpapers=kelly-brook)   

The naming convention for running sipder keyword argumets is small case first name and last name seperat2d by hypen (hrithik-roshan)    

The santabanta spider scrapes the wallpapers paged across for Hig Definition Images.     

This spider doesn't crawl the entire dmoz.org site but only a few pages by default (defined in the wallpapers attribute).     These pages are:    

http://www.santabanta.com/wallpapers    

So, if you run the spider,it will scrape only those pages only for wallpapers which are customized to save in settings.py (IMAGES_STORE).   

**<h3>Image Pipelines</h3>**      

This project uses a cutomized Image pipeline to rename images :    

santabanta.pipelines.MyImagesPipeline    
