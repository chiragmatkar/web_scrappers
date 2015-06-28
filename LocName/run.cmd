scrapy crawl ExternalLinkExtractor -a start_url=http://www.cairo360.com  -a domain=cairo360.com -o External.json
REM scrapy crawl InternalLinkExtractor -a start_url=http://www.cairo360.com -o Internal.json

REM scrapy crawl ExternalLinkExtractor -a start_url=http://eg.jeeran.com/en/cairo -a domain=jeeran.com -o External2.json
REM scrapy crawl InternalLinkExtractor -a start_url=http://eg.jeeran.com/en/cairo  -o Internal2.json

REM scrapy crawl ExternalLinkExtractor -a start_url=http://www.yellowpages.com.eg/en  -a domain=yellowpages.com.eg   -o External3.json
REM scrapy crawl InternalLinkExtractor -a start_url=http://www.yellowpages.com.eg/en -o Internal3.json


REM scrapy crawl Int-a start_url=http:http://www.cairo360.com   -o Int.json

REM scrapy crawl yellowpages -o yellowpages.json




