# FARA scraper

## Parses Foreign Agents Registration Act (FARA) for all [Active Foreign Principals by Country or Location](https://efile.fara.gov/pls/apex/f?p=185:130:0::NO:RP,130:P130_DATERANGE:N).

### Instructions:
Python3 scrapy-splash example.

I tested it only in Ubuntu 18.04, for lower versions of Ubuntu you may need to install python3 by yourself. 

If you are using different OS you need to figure out how to run it. Basic idea is simple: run docker and then run spider.

### How to run:
0. Get docker:

`sudo apt-get update && sudo apt-get install docker.io`

1. Run splash docker image:
(Downloading docker image if there is no such image):

`sudo docker run -p 8050:8050 scrapinghub/splash`

2. Open new terminal and install pip3:

`sudo apt-get update && sudo apt-get install python3-pip`

3. Then install virtualenv using pip3:

`sudo pip3 install virtualenv`

4. Create a virtual environment:

`cd Desktop && virtualenv -p /usr/bin/python3 venv`

5. Activate your virtual environment:

`source venv/bin/activate`

6. Inside your virtual environment install scrapy and scrapy-splash:

`pip install scrapy && pip install scrapy-splash`

7. *Run *main.py* in *FARA_scraper* folder:

`cd FARA_scraper/FARA_scraper/ && python main.py`

7. *OR run the same command from the terminal (*main.py* runs the same command):

`scrapy crawl 'FARA_scraper'`

*After that items.json file will be created or modified at *FARA_scraper/items.json*


The first problem was that all data was grouped by Country. To solve this problem I've had to uncheck the "Country/Location Represented" checkbox. After that, all rows had their own country.

The second problem was that you need to click "Next" to get the next portion of data. I've solved this problem by listing all the data in a single page via JavaScript command. After that, I could scrape all the data by only one request.
