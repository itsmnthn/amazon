# amazon
Skip to content
This repository
Search
Pull requests
Issues
Marketplace
Explore
 @ManthanSatani
 Sign out
 Watch 0
  Star 0
 Fork 0 ManthanSatani/amazon
 Code  Issues 0  Pull requests 0  Projects 1  Wiki  Settings Insights 
Branch: master Find file Copy pathamazon/AmazonScraper/README.txt
6ba6300  17 seconds ago
@ManthanSatani ManthanSatani Add files via upload
1 contributor
RawBlameHistory     
69 lines (48 sloc)  2.85 KB
*************     AmazonScraper     *************

Requirement to run the script...

	1. System - windows 7 or +
	2. python 2.7 (to install on windows follow this link https://www.python.org/downloads/)
	3. scrapy (to install on windows follow this link https://scraper24x7.wordpress.com/2016/03/19/how-to-install-scrapy-in-windows/)

File system of project and description

	AmazonScraper/
		- AmazonScraper/
			- spiders/
				- __init__.py
				- Amazon_Scraper.py
				- AmazonASINs.py
				- ASINsToIgnore.csv
				- KeywordsToIgnore.csv
				- out.csv
				- output.csv
			- __init__.py
			- items.py
			- middlewares.py
			- pipelines.py
			- settings.py
			- USER_AGENTS.txt
		- README.txt
		- scrapy.cfg

	---ASINsToIgnore.csv---
	put the ASINs that you want to ignore or don't want data from

	---KeywordsToIgnore.csv---
	put the keywords that you don't want data if it occurs in title or brand

	---Amazon_Scraper.py---
	run this spider if you have csv file with ASINs number that you have gathered data from amazon.ca
	this file will get the data from the amazon.com using ASINs and return csv file with final data after filtering all the requirements

	---AmazonASINs.py---
	run this spider before run the Amazon_Scrapper.py because this will gather the asins of given url

Run the script to follow the steps

	after all installation setup is done open command prompt and type following commands

		pip install scrapy-random-useragent

		open the setting file that is located at AmazonScraper/AmazonScraper/settings.py and replace the "Path to the USER_AGENTS.txt file" with path where USER_AGENTS.txt is stored AmazonScraper/AmazonScraper/USER_AGENTS.txt (note : full path ex - D:/AmazonScraper/AmazonScraper/USER_AGENTS.txt)

	--  AmazonASINs.py

		scrapy runspider AmazonASINs.py -o outputfilename.csv -a url="URL of amazon.ca"

		ex :- 
			scrapy runspider AmazonASINs.py -o ElectronicsASINs.csv -a url="https://www.amazon.ca/s/ref=lp_667823011_nr_p_6_8?fst=as%3Aoff&rh=n%3A667823011%2Cp_6%3AA3JVXPGY4Y8BM7&bbn=667823011&ie=UTF8&qid=1504720032&rnid=12035754011"

		it will generate the ElectronicsASINs.csv file in current directory that contains all the asins that are scraped now you can use this file as input to the Amazon_Scraper.py

	-- Amazon_Scraper.py

		scrapy runspider Amazon_Scraper.py -o outputfilename.csv -a csv=inputfilename.csv

		ex :-
			scrapy runspider .\Amazon_Scraper.py -o ElectronicsDATA.csv -a csv=ElectronicsASINs.csv

		it will generate the ElectronicsDATA.csv file in the current directory that contains ASINs, PRICE, TITLE, Brand, Shipping Weight, STOCK, Ship by, Category data columns with filtered data as per conditions

Note: if you want to use the both output file of script you must have to give diferent name each time or you can copy file to another location otherwise file will have currepted data.
© 2017 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
API
Training
Shop
Blog
About
